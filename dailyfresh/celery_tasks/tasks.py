from celery import Celery
from django.conf import settings
from django.core.mail import send_mail


# 在任务处理者一端加这几句
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
# django.setup()

app = Celery('celery_tasks.tasks',broker='redis://127.0.0.1:6379/1')

@app.task
def send_register_active_email(to_email,username,token):
    subject = '天天生鲜欢迎信息'
    message = ''
    sender = settings.EMAIL_FROM
    recever = [to_email]
    htmlmessage = '<h1>%s,欢迎您成为天天生鲜注册会员</h1>请点击下面链接激活您的用户</br><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
    username, token, token)
    send_mail(subject, message, sender, recever, html_message=htmlmessage)


