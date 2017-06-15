from django.conf.urls import url, include
from django.contrib import admin
from handover_items import views

app_name = 'handover_items'

urlpatterns = [
    #User Views on Handover
    url(r'^create/', views.create, name='create'),
    url(r'^all/', views.all, name='all'),
    url(r'^claimed/', views.claimed, name='claimed'),
    url(r'^unclaimed/', views.unclaimed, name='unclaimed'),
    url(r'^complete/', views.complete, name='complete'),

    #User actions on individual handover
    url(r'^details/(?P<handover_id>[0-9]+)/$', views.handover_details, name="handover_details"),
    url(r'^edit/(?P<handover_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^claim/(?P<handover_id>[0-9]+)/$', views.claim, name='claim'),
    url(r'^markcomplete/(?P<handover_id>[0-9]+)/$', views.markcomplete, name='markcomplete'),

    #User 'profile' view which shows all their own handover
    url(r'^user/(?P<fk>[0-9]+)/$', views.userposts, name='userposts'),

    #Primary Views
    url(r'^primary/home/', views.primary_home, name='primary_home'),
    url(r'^primary/all/', views.primary_all, name='primary_all'),
    url(r'^primary/claimed/', views.primary_claimed, name='primary_claimed'),
    url(r'^primary/unclaimed/', views.primary_unclaimed, name='primary_unclaimed'),
    url(r'^primary/complete/', views.primary_complete, name='primary_complete'),
    url(r'^primary/pending/', views.primary_need_approval, name='primary_need_approval'),
    url(r'^primary/approved/', views.primary_approved, name='primary_approved'),
    url(r'^primary/details/(?P<handover_id>[0-9]+)/$', views.primary_handover_details, name='primary_handover_details'),
    url(r'^primary/approve/(?P<handover_id>[0-9]+)/$', views.primary_approve, name='primary_approve'),
    url(r'^primary/deny/(?P<handover_id>[0-9]+)/$', views.primary_deny, name='primary_deny'),
]
