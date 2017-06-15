from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
import users.views
import handover_items.views

admin.site.site_title = 'RDS Handover Tool Admin'
admin.site.site_header = 'RDS Handover Tool Admin'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^handover/', include('handover_items.urls')),
    url(r'^$', handover_items.views.home, name='home'),

]
