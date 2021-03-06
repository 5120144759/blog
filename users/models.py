from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    icon = models.ImageField(upload_to='upload', default='')