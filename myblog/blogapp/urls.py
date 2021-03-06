from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    #url(r'^detail/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$',views.detail,name='detail'),这样可以传递多个参数
    url(r'^detail/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    url(r'^posts/$',views.posts,name='posts'),
    #第二个参数必须为函数
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='get_post_with_category'),

]
