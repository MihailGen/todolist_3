# tasks.py
from celery import shared_task
from todolist.models import Task
from datetime import datetime, timedelta, date


# Функция удаления из комментария запрещённых слов
@shared_task
def replace_bad_words_in_comment(comment):
    comment_is_changed = False
    for p in ['продать', 'крипта', 'ставки']:
        if p in comment.text:
            comment.text = comment.text.replace(p, '###')
            comment_is_changed = True
    print(comment.text)  # отладка
    if comment_is_changed:
        comment.save()


@shared_task
def change_deadtime():
    for tdt in Task.objects.filter(due_date__lt=datetime.date.today()):
        #tdt.due_date = date.today() + timedelta(days=1)
        print(tdt.name)
