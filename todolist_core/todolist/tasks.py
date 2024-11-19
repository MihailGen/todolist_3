# tasks.py
from celery import shared_task
from todolist.models import Task
from datetime import datetime, timedelta, date


@shared_task
def add(x, y):
    return x + y


@shared_task
def replace_bad_words_in_comment(comment):
    for p in ['продать', 'крипта', 'ставки']:
        if p in comment:
            comment = comment.replace(p, '###')
    return comment


@shared_task
def change_deadtime():
    for tdt in Task.objects.filter(due_date__lt=datetime.date.today()):
        tdt.due_date = date.today() + timedelta(days=1)
