from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta():
        db_table = 'category'

class Tags(models.Model):
    name = models.CharField(max_length=50)

    class Meta():
        db_table = 'tags'


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='upload')
    tags = models.ManyToManyField(Tags, blank=True)
    hot = models.IntegerField(default=0)
    view = models.IntegerField(default=0)

    class Meta():
        db_table = 'article'
