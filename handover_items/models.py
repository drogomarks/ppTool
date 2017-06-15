# -*- coding: utf-8 -*-sche
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Primary(models.Model):
    curernt_primary = models.ForeignKey(User)

class Region_Schedule(models.Model):
    sched_region = models.CharField(max_length=3, blank=True)
    region_times = models.CharField(max_length=20, blank=True)
    mon = models.CharField(max_length=20, blank=True)
    tues = models.CharField(max_length=20, blank=True)
    wed = models.CharField(max_length=20, blank=True)
    thurs = models.CharField(max_length=20, blank=True)
    fri = models.CharField(max_length=20, blank=True)
    sat = models.CharField(max_length=20, blank=True)
    sun = models.CharField(max_length=20, blank=True)
    region_manager = models.CharField(max_length=20, blank=True)
    region_TL1 = models.CharField(max_length=20, blank=True)
    region_TL2 = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.sched_region

class Handover(models.Model):

    # Get ready...gonna set a lot of vars

    #Set Vars for Support Level choices
    ent = 'Enterprise'
    bus = 'Business'
    dev = 'Developer'
    SUPPORT_CHOICES = (
        (ent, 'Enterprise'),
        (bus, 'Business'),
        (dev, 'Developer'),
    )

    #Set vars for Sev Level choices
    five = '5'
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    SEV_CHOICES = (
        (five, '5'),
        (one, '1'),
        (two, '2'),
        (three, '3'),
        (four, '4'),
    )

    #Set vars for Engine/Service Types
    mysql = 'MySQL'
    mssql = 'SQL Server'
    aurora = 'Aurora'
    maria = 'MariaDB'
    postgres = 'PostgreSQL'
    redshift = 'Redshift'
    dms = 'DMS'
    ENGINE_CHOICES = (
        (mysql, 'MySQL'),
        (mssql, 'SQL Server'),
        (aurora, 'Aurora'),
        (maria, 'MariaDB'),
        (postgres, 'PostgreSQL'),
        (redshift, 'Redshift'),
        (dms, 'DMS'),
    )

    #Set Vars for Regions
    sea = 'SEA'
    syd = 'SYD'
    dfw = 'DFW'
    iad = 'IAD'
    dub = 'DUB'
    cpt = 'CPT'

    REGION_CHOICES = (
        (sea , 'SEA'),
        (syd, 'SYD'),
        (dfw, 'DFW'),
        (iad, 'IAD'),
        (cpt, 'CPT'),
        (dub, 'DUB'),
    )

    #Set vars for Status choices
    active = 'Active (Action Needed)'
    pending_customer = 'Pending Customer Response'
    pending_amazon = 'Pending Amazon Response (TT)'
    complete = 'Complete'
    STATUS_CHOICES = (
        (active, 'Active (Action Needed)'),
        (pending_customer, 'Pending Customer Response'),
        (pending_amazon, 'Pending Amazon Response (TT)'),
        (complete, 'Complete'),

    )


    approved = models.BooleanField(default=False)
    claimed = models.BooleanField(default=False)

    # Things for initial creation by author/submitter
    owner = models.ForeignKey(User)
    created_date = models.DateTimeField(default=timezone.now)

    # Core items of a handover that will probably not not change
    support_level = models.CharField(max_length=10, choices=SUPPORT_CHOICES)
    sev_level = models.CharField(max_length=1, choices=SEV_CHOICES)
    engine = models.CharField(max_length=10, choices=ENGINE_CHOICES)
    case_link = models.URLField(max_length=100)
    related_item1 = models.URLField(max_length=100, blank=True)
    related_item2 = models.URLField(max_length=100, blank=True)
    related_item3 = models.URLField(max_length=100, blank=True)
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    notes = models.TextField()


    # Handover items that will change
    from_region = models.CharField(max_length=3, choices=REGION_CHOICES, default=sea)
    to_region =  models.CharField(max_length=3, choices=REGION_CHOICES,default=syd)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=active)
    last_updated = models.DateTimeField(default=timezone.now, blank=True)
    primary_approval_notes = models.TextField(blank=True)
    primary_denial_notes = models.TextField(blank=True)
    primary_notes = models.TextField(blank=True)
    current_owner = models.CharField(max_length=20, blank=True)
    owner_hist = models.CharField(max_length=256, blank=True)

    # Pretty print the date
    def created_date_pretty(self):
        return '%s @ %s' % (self.created_date.strftime('%b %e, %Y'), self.created_date.strftime('%H:%M %Z'))

    def last_updated_pretty(self):
        return '%s @ %s' % (self.last_updated.strftime('%b %e, %Y'), self.last_updated.strftime('%H:%M %Z'))

    # Readable Title for object in /admin
    def __str__(self):
        return 'Submitted by %s on   %s at %s' % (self.owner, self.created_date.strftime('%b %e, %Y'), self.created_date.strftime('%H:%M %p %Z'))
