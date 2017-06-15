from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^register/$',views.regester,name='register'),
    url(r'^login/$',views.signin,name='login'),
    url(r'^logout/$',views.signout,name='logout'),

]
