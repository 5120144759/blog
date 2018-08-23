from django.conf.urls import url
from myBlog import views

urlpatterns = [
    # url(r'', views.index ,name='index'),
    # 博客详情页
    url(r'^info/(?P<cid>\d+)$', views.info, name='info')
]