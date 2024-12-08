# tasks.py
from datetime import datetime
from celery import shared_task
from .models import Task


# Функция удаления из комментария запрещённых слов
@shared_task
def replace_bad_words_in_comment(comment):
    comment_is_changed = False
    for p in ['продать', 'крипта', 'ставки']:
        if p in comment.text:
            comment.text = comment.text.replace(p, '###')
            print(comment.text)
            # comment.text.replace(p, '###')
            comment_is_changed = True
    print(comment.text)  # отладка
    if comment_is_changed:
        comment.save()


@shared_task
def change_deadtime():
    for tdt in Task.objects.filter(due_date__lt=datetime.date.today()):
        tdt.due_date = datetime.date.today() + datetime.timedelta(days=1)
        print(tdt.name)
