# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from handover_items.models import Primary
import datetime
from django.utils import timezone
from handover_items.models import Primary
from handover_items.models import Region_Schedule

def register(request):
    #Make sure the request is a POST
    if request.method == 'POST':
        #If it is, then make sure that password1 and 2 match (from the form)
        if request.POST['password1'] == request.POST['password2']:
            #See if this user has already registered
            try:
                user = User.objects.get(username=request.POST['alias'])
                return render(request, 'users/register.html', {'error':'Oops! Looks like this Alias has already been registered.'})
            #If the user has not been registered then create the user
            except User.DoesNotExist:
                User.objects.create_user(request.POST['alias'], password=request.POST['password1'])
                return render(request, 'users/login.html', {'success':'Yay! Your all registered. You can now claim and submit handover. :D'})
        #If the the passwords don't match, error
        else:
            return render(request, 'users/register.html', {'error':'Passwords don\'t match. No bueno.'})
    #IF the request is NOT POST (probably get) then just show the page. :)
    else:
        return render(request, 'users/register.html')



def loginview(request):
    #If the request method is a POST
    if request.method == 'POST':
        #Authenticate the user
        user = authenticate(request, username=request.POST['alias'], password=request.POST['password'])
        #Log the user in
        if user is not None:
            login(request, user)
            #Send the user to the orginally requested page.
            if 'next' in request.POST:
               return redirect(request.POST['next'])
            # if successful reload the page and display success message
            return render(request, 'users/login.html', {'success': 'Success!'})

        else:
            #If the login fails then show this
            return render(request, 'users/login.html', {'error': "Your alias or password is incorrect."})
    else:
        #If the request method is not POST (probably GET) then just show the page
        return render(request, 'users/login.html')

def logoutview(request):
    #If the request is a POST
    if request.method == 'POST':
        #Logout the user
        logout(request)
        #Then return them home
        return redirect('home')


def userprofile(request, alias):
    user = User.objects.get(username=alias)
    return render(request, 'users/profile.html')

@login_required
def login_as_primary(request):

    if request.method == 'POST':
        user = request.user
        Primary.objects.update(curernt_primary=user)
        return redirect('handover_items:primary_home')

    else:

        now = datetime.datetime.now()
        current_day = now.strftime("%A")
        if current_day == "Monday":
            current_day = 'mon'
        elif current_day == "Tuesday":
            current_day = 'tues'
        elif current_day == "Wednesday":
            current_day = 'wed'
        elif current_day == "Thursday":
            current_day = 'thurs'
        elif current_day == "Friday":
            current_day = 'fri'
        elif current_day == "Saturday":
            current_day = 'sat'
        elif current_day == "Sunday":
            current_day = 'sun'

        current_primary = Region_Schedule.objects.filter(sched_region='SEA').values_list(current_day)

        return render(request, 'users/primary_login.html', {'current_primary' : current_primary, 'current_day' : current_day})



def primary_login(request):
    #If the request method is a POST
    if request.method == 'POST':
        #Authenticate the user
        user = authenticate(request, username=request.POST['alias'], password=request.POST['password'])
        #Log the user in
        if user is not None:
            login(request, user)
            # if successful reload the page and display success message
            return render(request, 'handover_items/primary_need_approval.html', {'success' : 'You are now logged in as Primary'})

        else:
            #If the login fails then show this
            return render(request, 'users/primary_login.html', {'error': "Your alias or password is incorrect."})
    else:
        #If the request method is not POST (probably GET) then just show the page
        return render(request, 'users/primary_login.html')
