

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^author/',views.blog_detail,name='blog_detail'),
    url(r'^blog/(?P<pk>\d+)/',views.author_detail,name='author_detail'),
    url(r'^authorname',views.author,name='author'),
    url(r'^article',views.article,name='article'),

]