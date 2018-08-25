from django.core import paginator
from django.shortcuts import render


# Create your views here.
from myBlog.models import Article, Tags, Category


def index(request):
    articles = Article.objects.all().order_by('-create_time')
    tags = Tags.objects.all()
    categorys = Category.objects.all()
    ctx = {'articles': articles,
           'tags': tags,
           'categorys': categorys}
    return render(request, 'index.html', ctx)


def info(request, cid):
    article = Article.objects.get(pk=cid)
    tags = Tags.objects.filter(article=article).all()
    return render(request, 'info.html', {'article': article, 'tags': tags})
