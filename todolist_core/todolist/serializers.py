from rest_framework import serializers
from .models import Task, Comment, Tag
from .utils import get_cached_tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer): #класс сериализер до кэширования
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'comments']

    def get_comments_count(self, obj):
        return obj.comments.count()


'''class TaskSerializer(serializers.ModelSerializer):  #класс сериализер c кэшированием
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'tags']

    def get_tags(self, obj):
        tags = get_cached_tags(obj.id)
        return [tag.name for tag in tags]'''