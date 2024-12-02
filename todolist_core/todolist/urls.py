from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TodolistViewSet, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView, TagListView, \
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, CategoryViewSet, CommentViewSet, CommentCreateView, \
    CommentListView , CommentRetrievView, CommentUpdateView, CommentDestroyView

app_name = 'tasks'

router = DefaultRouter()
router.register(r'tasks', TodolistViewSet)
#router.register(r'tags', TagViewSet)
#router.register(r'tags', TagListView)
router.register(r'category', CategoryViewSet)
#router.register(r'comments', CommentViewSet)

router.register(r'comments/create/', CommentCreateView)
#router.register(r'comments/', CommentListView)
#router.register(r'comments/<int:pk>/', CommentRetrievView)
#router.register(r'comments/<int:pk>/update/', CommentUpdateView)
#router.register(r'comments/<int:pk>/delete/', CommentDestroyView)

urlpatterns = [
    # path('comments/', CommentListCreateAPIView.as_view()),
    # path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
    #path('', include(router.urls)),
    #path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('tags/', TagListView.as_view(), name='get_tags'),
    path('tags/<int:pk>/', TagListView.as_view(), name='tag-retrieve'),
    path('comments/<int:pk>/', CommentRetrievView.as_view(), name='comment-retrieve'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDestroyView.as_view(), name='comment-destroy'),

    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),

] + router.urls
