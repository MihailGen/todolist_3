from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TodolistViewSet, TagListView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, \
    CategoryViewSet, CommentCreateView, CommentListView, CommentRetrievView, CommentUpdateView, CommentDestroyView

app_name = 'tasks'
router = DefaultRouter()
router.register(r'tasks', TodolistViewSet, basename='tasks')
router.register(r'category', CategoryViewSet)
urlpatterns = [
                  path('', include(router.urls)),
                  path('tags/', TagListView.as_view(), name='tags-list'),
                  path('tags/<int:pk>/', TagListView.as_view(), name='tag-retrieve'),
                  path('comments/', CommentListView.as_view(), name='comment-list'),
                  path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
                  path('comments/<int:pk>/', CommentRetrievView.as_view(), name='comment-retrieve'),
                  path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
                  path('comments/<int:pk>/delete/', CommentDestroyView.as_view(), name='comment-destroy'),
                  path('category/', CategoryListCreateAPIView.as_view()),
                  path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),

              ] + router.urls
