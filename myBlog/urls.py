from django.conf.urls import url
from myBlog import views

urlpatterns = [
    # url(r'', views.index ,name='index'),
    # 博客详情页
    url(r'^info/$', views.info, name='info'),
    # 博客分类
    url(r'^category/(?P<cid>\d+)$', views.category, name='category'),
    # 标签
    url(r'^tags/(?P<tid>\d+)$', views.tags, name='tags'),

]