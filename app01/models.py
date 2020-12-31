from django.db import models
# python manage.py makemigrations 制作迁移文件倒app01/migrations/0001_initial.py
# python manage.py migrate  同步到数据库
class User(models.Model):
    username = models.CharField(max_length=32)  # CharField对应varchar类型
    password = models.CharField(max_length=32)  # varchar(32)
