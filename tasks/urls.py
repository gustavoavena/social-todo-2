from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'up', views.say_whatsup, name='whatsup'),
    url(r'create', views.create, name='create'),
    url(r'complete', views.complete, name='complete'),
    url(r'remove', views.remove, name='remove'),
]


