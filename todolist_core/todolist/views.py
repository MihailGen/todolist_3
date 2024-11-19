from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, mixins
from .models import Task, Comment, Tag
from .serializers import TaskSerializer, CommentSerializer, TagSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from .models import Tag
from .serializers import TagSerializer
from django.http import JsonResponse
from .tasks import add
from todolist.tasks import replace_bad_words_in_comment


def base(request):
    return render(request, 'todolist/base.html')


class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self):
        self.text = replace_bad_words_in_comment(self.text)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


@method_decorator(cache_page(60 * 15), name='get')
class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


def add_view(request):
    result = add.delay(4, 4)
    return JsonResponse({'task_id': result.id})
