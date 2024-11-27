from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория задачи')
    color = models.CharField(max_length=50, verbose_name='Цвет отметки задачи')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=150, verbose_name='Тема задачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Cроки выполнения')
    author = models.CharField(max_length=50, null=True, blank=True, verbose_name='Автор')
    tags = models.ManyToManyField('Tag', related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', null=True, blank=True)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return self.name


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.id}, "{self.text}", on {self.created_at}'


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name
