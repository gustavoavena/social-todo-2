from django.conf.urls import url

from . import views


#these are the url patterns for the users subapp.
urlpatterns = [
    url(r'register', views.register, name='register'),
    url(r'login', views.login_user, name='login'),
    url(r'logout', views.logout_user, name='logout'),
    url(r'dashboard', views.dashboard, name='dashboard'),

]

