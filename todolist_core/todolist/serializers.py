from rest_framework import serializers

from .models import Task, Comment, Tag, Category
from .utils import get_cached_tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Task
        # fields = ['id', 'name', 'description', 'tags']
        fields = '__all__'
    def get_tags(self, obj):
        tags = get_cached_tags(obj.id)
        return [tag.name for tag in tags]


class CategorySerializer(serializers.ModelSerializer):  # класс сериализер до кэширования
    tasks = TaskSerializer(many=True, read_only=False, default=1)
    class Meta:
        model = Category
        fields = ['id', 'name', 'color']
