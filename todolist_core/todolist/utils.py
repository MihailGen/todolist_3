from django.core.cache import cache
from .models import Tag


def get_cached_tags(task_id):
    key = f'tags_for_task_{task_id}'
    tags = cache.get(key)
    if not tags:
        tags = list(Tag.objects.filter(task__id=task_id))
        cache.set(key, tags, 60 * 15)  # Кешируем на 15 минут
    return tags
