from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^([0-9]+)/$',views.detail,name='detail')
]