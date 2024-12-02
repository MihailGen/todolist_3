from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, mixins
from .models import Task, Comment, Tag
from .serializers import TaskSerializer, CommentSerializer, TagSerializer, CategorySerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from .models import Tag
from .models import Category
from .serializers import TagSerializer
from django.http import JsonResponse
from .tasks import add
from .tasks import replace_bad_words_in_comment


def base(request):
    return render(request, 'todolist/base.html')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = TagSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


'''
class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self):
        self.text = replace_bad_words_in_comment(self.text)

'''


class CommentCreateView(viewsets.ModelViewSet):  # БЫЛ generics.CreateAPIView
    # Класс-контроллер для создани объектов модели Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer_class):
        instance = serializer_class.save()
        # instance.text = replace_bad_words_in_comment.delay(instance.text)
        instance.text = replace_bad_words_in_comment(instance.text)
        #serializer_class.save(instance)
        print(f'!!!!!!{instance.id}!!!{instance.text}')
        print('!!!!! ЭТО_РАБОТАЕТ !!!!!!!!')


class CommentListView(generics.ListAPIView):
    # Класс-контроллер для просомтра списка объектов модели Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrievView(generics.RetrieveAPIView):
    # Класс-контроллер для просмотра отдельного объекта модели Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(generics.UpdateAPIView):
    # Класс-контроллер для редактирования объектов модели Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyView(generics.DestroyAPIView):
    # Класс-контроллер для удаления объектов модели Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


'''
@method_decorator(cache_page(60 * 15), name='get')
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
'''


# Контроллер для работы со списком тегов + декоратор кеширования:
@method_decorator(cache_page(60 * 15), name='get')
class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


def add_view(request):
    result = add.delay(4, 4)
    return JsonResponse({'task_id': result.id})
