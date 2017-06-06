from django.conf.urls import url
from . import views

#app_name='comments'同项目下urls.py中的namespa
urlpatterns=[
    url(r'^post_comment/(?P<post_pk>[0-9]+)/$',views.post_comment,name='post_comment'),
            ]
