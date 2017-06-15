from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.loginview, name='login'),
    url(r'^logout/', views.logoutview, name='logout'),

    #Primary
    url(r'^primary/login/', views.primary_login, name='primary_login'),
    url(r'^primary/loginas/', views.login_as_primary, name='login_as_primary'),
]
