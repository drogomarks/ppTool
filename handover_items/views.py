# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .models import Handover
from .models import Primary
from .models import Region_Schedule



def home(request):
    return redirect('handover_items:unclaimed')

def all(request):
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

    handovers = Handover.objects.filter(approved=True).order_by('-created_date')
    return render(request, 'handover_items/all.html', {'handovers': handovers, 'current_primary' : current_primary})

def claimed(request):
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

    handovers = Handover.objects.filter(claimed=True, approved=True).order_by('-created_date').exclude(status="Complete")
    return render(request, 'handover_items/claimed.html', {'handovers': handovers, 'current_primary' : current_primary})

def unclaimed(request):
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

    handovers = Handover.objects.filter(claimed=False, approved=True).order_by('-created_date').exclude(status="Complete")
    return render(request, 'handover_items/unclaimed.html', {'handovers': handovers, 'current_primary' : current_primary})

def complete(request):
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

    handovers = Handover.objects.filter(status="Complete", approved=True).order_by('-created_date')
    return render(request, 'handover_items/complete.html', {'handovers': handovers, 'current_primary' : current_primary})

def handover_details(request, handover_id):

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


    handover = get_object_or_404(Handover, pk=handover_id)
    return render(request, 'handover_items/handover_details.html', {'handover':handover, 'current_primary' : current_primary})

######## Primay stuff  #####

def primary_home(request):
    return redirect('handover_items:primary_need_approval')

def primary_need_approval(request):

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


    handovers = Handover.objects.filter(approved=False).order_by('-created_date').exclude(status="Complete")
    return render(request, 'handover_items/primary_need_approval.html', {'handovers': handovers, 'current_primary' : current_primary})

def primary_approved(request):

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


    handovers = Handover.objects.filter(approved=True).order_by('-created_date').exclude(status="Complete")
    return render(request, 'handover_items/primary_approved.html', {'handovers': handovers, 'current_primary' : current_primary})

def primary_all(request):
    handovers = Handover.objects.order_by('-created_date')
    return render(request, 'handover_items/primary_all.html', {'handovers': handovers})

def primary_claimed(request):
    handovers = Handover.objects.filter(claimed=True).order_by('-created_date').exclude(status="Complete")
    return render(request, 'handover_items/primary_claimed.html', {'handovers': handovers})

def primary_unclaimed(request):
    handovers = Handover.objects.filter(claimed=False).order_by('-created_date').exclude(status="Complete")
    return render(request, 'handover_items/primary_unclaimed.html', {'handovers': handovers})

def primary_complete(request):
    handovers = Handover.objects.filter(status="Complete").order_by('-created_date')
    return render(request, 'handover_items/primary_complete.html', {'handovers': handovers})

def primary_handover_details(request, handover_id):

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

    handover = get_object_or_404(Handover, pk=handover_id)
    return render(request, 'handover_items/primary_handover_details.html', {'handover':handover, 'current_primary' : current_primary})

def primary_approve(request, handover_id):
    if request.method == 'POST':
        handover = get_object_or_404(Handover, pk=handover_id)

        new_notes = request.POST.get('approval_notes')
        Handover.objects.filter(pk=handover_id).update(approved=True, primary_approval_notes=new_notes)
        return render(request, 'handover_items/primary_handover_details.html', {'handover':handover , 'success':'Handover approved.'})
    else:
        handover = get_object_or_404(Handover, pk=handover_id)
        return render(request, 'handover_items/primary_handover_details.html', {'handover':handover})

def primary_deny(request, handover_id):
    if request.method == 'POST':
        handover = get_object_or_404(Handover, pk=handover_id)

        if request.POST.get('denial_notes'):
            new_notes = request.POST.get('denial_notes')
            Handover.objects.filter(pk=handover_id).update(approved=False, primary_denial_notes=new_notes)
            return render(request, 'handover_items/primary_handover_details.html', {'handover':handover , 'deny':'Handover denied. Notes sent to owner.'})
        else:
            return render(request, 'handover_items/primary_handover_details.html', {'handover':handover , 'error':'Notes required to Deny!'})
    else:
        handover = get_object_or_404(Handover, pk=handover_id)
        return render(request, 'handover_items/primary_handover_details.html', {'handover':handover})


###### End Primary stuff #########


@login_required
def create(request):

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


    current_user = request.user
    current_user_email = "%s@amazon.com" % current_user

    current_primary_email = "%s@amazon.com" % current_primary

    # If the method is POST
    if request.method == 'POST':
        # AND the user is posting required items.
        if request.POST['case_link']:
            handover = Handover()
            handover.owner = request.user
            handover.pub_date =  timezone.datetime.now()

            handover.support_level = request.POST['support_level']
            handover.sev_level = request.POST['sev_level']
            handover.engine = request.POST['engine']

            handover.case_link = request.POST['case_link']

            handover.related_item1 = request.POST['related_item1']
            handover.related_item2 = request.POST['related_item2']
            handover.related_item3 = request.POST['related_item3']

            handover.attachment = request.POST['attachment']
            handover.status = request.POST['status']
            handover.notes = request.POST['notes']

            handover.save()

            #Email to Requestor
            send_mail(
                'Handover Submitted',
                'Your Handover was submtted for review by the Profile Primary.\nYou will be notified when it is approved or denied via Email.\nYou can review and edit your handover by clicking the drop down in the uppper right navbar with your name and selecting "Your Hanodver".\n\nHere is what you submitted:\n\nSeverity: %s \n\nSupport Level: %s \n\nEngine: %s \n\nStatus: %s \n\nNotes: %s' % (handover.sev_level, handover.support_level, handover.engine, handover.status, handover.notes),
                'localhost@localhost.com',
                [current_user_email],
                fail_silently=False,
            )

            #Email to Primary
            send_mail(
                'New Handover Submitted for Approval!',
                'A new handover was submitted by %s: \n \nSeverity: %s \n\nSupport Level: %s \n\nEngine: %s \n\nStatus: %s \n\nNotes: %s' % (handover.owner, handover.sev_level, handover.support_level, handover.engine, handover.status, handover.notes ),
                'localhost@localhost.com',
                [current_primary_email],
                fail_silently=False,
            )

            return render(request, 'handover_items/create.html', {'success' : 'Handover submitted for approval by Primary.', 'current_primary' : current_primary })
        else:
            return render(request, 'handover_itmes/create.html', {'error' : 'ERROR: Case Link is required to create a handover item.', 'current_primary' : current_primary})
    else:
        return render(request, 'handover_items/create.html', {'current_primary' : current_primary})

def userposts(request, fk):
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


    handovers = Handover.objects.filter(owner__id=fk).order_by('-created_date')
    owner = User.objects.get(pk=fk)
    return render(request, 'handover_items/userposts.html', {'handovers':handovers, 'owner': owner, 'current_primary':current_primary })

@login_required
def claim(request, handover_id):
    if request.method == 'POST':
        #Load up some dem variables with stuff from that there derterbers
        new_owner = str(request.user)
        db_owner = Handover.objects.filter(pk=handover_id).values_list('current_owner', flat=True).order_by('id')
        db_hist = Handover.objects.filter(pk=handover_id).values_list('owner_hist', flat=True).order_by('id')
        old_hist = str(db_hist[0])
        curr_owner = str(db_owner[0])

        #if the item is not yet owned, don't bother updating the history, otherwise do!
        if len(curr_owner) == 0:
            handover_updated = Handover.objects.filter(pk=handover_id).update(current_owner=new_owner, owner=request.user)
        else:
            #If the history field is blank just add the last person to have owned it, otherwise update the list
            if len(old_hist) == 0:
                new_hist = curr_owner
            else:
                new_hist = old_hist + ", " + curr_owner
            handover_updated = Handover.objects.filter(pk=handover_id).update(current_owner=new_owner, owner=request.user, owner_hist=new_hist)

        Handover.objects.filter(pk=handover_id).update(claimed=True)
        handover = get_object_or_404(Handover, pk=handover_id)
        return render(request, 'handover_items/handover_details.html', {'handover':handover, 'success' : 'Successfully claimed.'})
    else:
        handover = get_object_or_404(Handover, pk=handover_id)
        return render(request, 'handover_items/handover_details.html', {'handover':handover})

@login_required
def edit(request, handover_id):
    if request.method == 'POST':
        handover = get_object_or_404(Handover, pk=handover_id)

        last_updated = timezone.datetime.now()
        new_support_level = request.POST['support_level']
        new_sev_level = request.POST['sev_level']
        new_from_region = request.POST['from_region']
        new_to_region = request.POST['to_region']
        new_engine = request.POST['engine']

        new_case_link = request.POST['case_link']

        new_related_item1 = request.POST['related_item1']
        new_related_item2 = request.POST['related_item2']
        new_related_item3 = request.POST['related_item3']

        new_attachment = request.POST['attachment']
        new_status = request.POST['status']
        new_notes = request.POST['notes']

        Handover.objects.filter(pk=handover_id).update(
            last_updated=last_updated,
            support_level=new_support_level,
            sev_level=new_sev_level,
            engine=new_engine,
            from_region=new_from_region,
            to_region=new_to_region,
            case_link=new_case_link,
            related_item1=new_related_item1,
            related_item2=new_related_item2,
            related_item3=new_related_item3,
            attachment=new_attachment,
            status=new_status,
            notes=new_notes,
            )

        handover = get_object_or_404(Handover, pk=handover_id)

        return render(request, 'handover_items/handover_details.html', {'handover':handover , 'success':'Handover Successfully Updated!'})
    else:
        handover = get_object_or_404(Handover, pk=handover_id)
        return render(request, 'handover_items/edit.html', {'handover':handover})

@login_required
def markcomplete(request, handover_id):
    if request.method == 'POST':
        handover_updated = Handover.objects.filter(pk=handover_id).update(status="Complete")
        handover = get_object_or_404(Handover, pk=handover_id)
        return render(request, 'handover_items/handover_details.html', {'handover':handover, 'success' : 'Marked as Completed.'})
    else:
        handover = get_object_or_404(Handover, pk=handover_id)
        return render(request, 'handover_items/handover_details.html', {'handover':handover})

