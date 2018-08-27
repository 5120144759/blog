from django.core import paginator
from django.core.paginator import Paginator
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


def info(request):
    cid = request.GET.get('cid', 1)
    article_list = Article.objects.all()
    article = Article.objects.get(pk=cid)
    paginator = Paginator(article_list, 1)
    page = paginator.page(cid)
    article.view += 1
    article.save()
    if page.has_next():
        article_next = Article.objects.filter(pk=page.next_page_number()).first()
        if page.has_previous():
            article_pre = Article.objects.filter(pk=page.previous_page_number()).first()
            return render(request, 'info.html', {'article_list': page,
                                                 'article_next': article_next,
                                                 'article_pre': article_pre})
        else:
            return render(request, 'info.html', {'article_list': page,
                                                 'article_next': article_next,})
    elif page.has_previous():
        article_pre = Article.objects.filter(pk=page.previous_page_number()).first()
        return render(request, 'info.html', {'article_list': page,
                                             'article_pre': article_pre})
    return render(request, 'info.html', {'article_list': page, 'tags': tags})


def category(request, cid):
    articles = Article.objects.filter(category_id=cid).order_by('-create_time')
    tags = Tags.objects.all()
    categorys = Category.objects.all()
    ctx = {'articles': articles,
           'tags': tags,
           'categorys': categorys}
    return render(request, 'index.html', ctx)


def tags(request, tid):
    articles = []
    tag = Tags.objects.get(pk=int(tid))
    for article in Article.objects.all():
        if tag in article.tags.all():
            articles.append(article)
    tags = Tags.objects.all()
    categorys = Category.objects.all()
    ctx = {'articles': articles,
           'tags': tags,
           'categorys': categorys}
    return render(request, 'index.html', ctx)





