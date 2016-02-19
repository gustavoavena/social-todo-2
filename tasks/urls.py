from django.conf.urls import url

from . import views

#These are the URL patterns for the tasks subapp.
urlpatterns = [
    url(r'create', views.create, name='create'),
    url(r'complete', views.complete, name='complete'),
    url(r'remove', views.remove, name='remove'),
]


