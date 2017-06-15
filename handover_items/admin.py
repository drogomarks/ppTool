# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Handover
from .models import Region_Schedule

admin.site.register(Handover)
admin.site.register(Region_Schedule)
