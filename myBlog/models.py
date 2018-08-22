from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

class Tags(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta():
        db_table = 'tags'


class column(models.Model):
    title = models.CharField(max_length=50)
    content = models.Text()
    create_time = models.DateTimeField(auto_now_add=True)

