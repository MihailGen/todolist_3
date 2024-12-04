from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Task, Comment, Tag
from .serializers import TaskSerializer, CommentSerializer, TagSerializer, CategorySerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from .models import Category
from .tasks import replace_bad_words_in_comment


def base(request):
    tasks = Task.objects.all()
    return render(request, 'todolist/base.html', {'tasks': tasks})


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


class CommentCreateView(generics.CreateAPIView):  # БЫЛ viewsets.ModelViewSet
    # Класс-контроллер для создани объектов модели Comment
    queryset = Comment.objects.all()
    # Запуск функции очистки комментариев от запрещённых слов
    serializer_class = CommentSerializer

    def perform_create(self, serializer_class):
        instance = serializer_class.save()
        replace_bad_words_in_comment.delay(instance)
        #replace_bad_words_in_comment(instance)


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


# Контроллер для работы со списком тегов + декоратор кеширования:
@method_decorator(cache_page(60 * 15), name='get')
class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
