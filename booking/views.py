from django.shortcuts import render,redirect
from django.db import models
from booking.models import Booking
from .forms import BookingCreateForm, CandidateSearchForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta,date
from datetime import datetime, timedelta,date
from riskAssesment.models import Symptoms, Hygiene, Travel, Screening
from riskAssesment.forms import SymptomsForm, TravelForm, HygieneForm


def booking_view(request):
   
    queryset = Booking.objects.all().count()
    form = BookingCreateForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }

    if request.method == 'POST':

        queryset = Booking.objects.all().order_by('booked_date').filter(booked_date__iexact=form['booked_date'].value()).filter(status__iexact="Approved").filter(status__iexact="Pending")
       
        context = {
            "queryset" : queryset,
            "form" : form,
        }
        occupied = queryset.count()

        
       

        if form.is_valid():
            myDate = datetime.now()
            tomorrow = myDate + timedelta(days=1)
            today = myDate.strftime("%A")
            tomorrow = tomorrow.strftime("%A")

            date= form['booked_date'].value()
            
       
            date_entry = form['booked_date'].value()
            year,month,day = map(int, date_entry.split('-'))
            now = datetime(year,month,day).date()
            
           
           
            day = now.strftime("%A")
            user = Booking.objects.all().filter(booked_date__iexact=now).filter(user_id=request.user).count()

            if day == today or day == tomorrow:
                messages.error(request, 'You can only book your date 48 hours in advance !' )
            else:

                if user >= 1:
                    messages.error(request, 'You already Booked this Day !' )
                else:

                    if  day == "Monday":
                        min_day=now
                        max_day = now + timedelta(days=4)
                    elif day =="Tuesday":
                        min_day= now - timedelta(days=1)
                        max_day = now + timedelta(days=3)

                    elif day =="Wednesday":
                        min_day= now - timedelta(days=2)
                        max_day = now + timedelta(days=2)
                    elif day =="Thursday":
                        min_day= now - timedelta(days=3)
                        max_day = now + timedelta(days=1)
                    elif day =="Friday":
                        min_day= now - timedelta(days=4)
                        max_day = now 

                    else:
                        messages.error(request, 'Can only book week days e.g Monday-Friday!' )
                        return redirect('booking')

                    week = Booking.objects.all().filter(booked_date__gte=min_day).filter(booked_date__lte=max_day).filter(user_id=request.user).count()

                    
                    if week >= 3:
                        messages.error(request, 'Sorry! you already booked three times this week '  )
                    else:

                        if occupied >= 30:
                            messages.error(request, 'Sorry! Space is already full on ' + day + ' ('+ date_entry +')' + '  try to Book for another Day , Thank You' )
                        else:
                            symptoms = Symptoms.objects.latest("user_id")
                            hygiene = Hygiene.objects.latest("user_id")
                            travel = Travel.objects.latest("user_id")
                            screening = Screening.objects.latest("user_id")
                            
                            instance = form.save(commit = False)
                            if hygiene.status =="Low Risk" or travel.status =="Low Risk" or symptoms.status =="Low Risk":
                                instance .status = "Pending"
                                instance.user = request.user
                                instance.Screening_id = screening.id
                                instance.save()
                                return redirect('pending')
                            else:
                                instance .status = "Approved"
                                instance.user = request.user
                                instance.Screening_id = screening.id
                                instance.save()
                                return redirect('approved')
        
        
            
    return render(request,'booking/booking.html',context)

def admin_view(request):
    queryset = Booking.objects.all().order_by('booked_date').filter(status__iexact="Approved").filter(booked_date__iexact=date.today())
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }

    if request.method == 'POST':
        queryset = Booking.objects.all().order_by('booking_date').filter(booked_date__icontains=form['booked_date'].value()).filter(status__iexact="Approved")
        context = {
            "queryset" : queryset,
            "form" : form,
        }
    return render(request,'booking/admin_page.html',context)




def admin_pending(request):
    queryset = Booking.objects.all().order_by('booked_date').order_by('booked_date').filter(status__iexact="Pending")
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }
    if request.method == 'POST':
        if form['booked_date'] =="":
            return redirect('view_user')
        else:
            queryset = Booking.objects.all().filter(booked_date__icontains=form['booked_date'].value()).filter(status__iexact="Pending")
            context = {
                "queryset" : queryset,
                "form" : form,
            }
    return render(request,'booking/admin_pending.html',context)

def admin_approved(request):
    queryset = Booking.objects.all().order_by('booked_date').filter(status__iexact="Approved")
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }
    if request.method == 'POST':
        if form['booked_date'] =="":
            return redirect('view_user')
        else:
            queryset = Booking.objects.all().order_by('booked_date').filter(booked_date__icontains=form['booked_date'].value()).filter(status__iexact="Approved")
            context = {
                "queryset" : queryset,
                "form" : form,
            }
    return render(request,'booking/admin_approved.html',context)

def admin_rejection(request):
    queryset = Booking.objects.all().order_by('booked_date').filter(status__iexact="Rejected")
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }
    if request.method == 'POST':
        if form['booked_date'] =="":
            return redirect('view_user')
        else:
            queryset = Booking.objects.all().order_by('booked_date').filter(booked_date__icontains=form['booked_date'].value()).filter(status__iexact="Rejected")
            context = {
                "queryset" : queryset,
                "form" : form,
            }
    return render(request,'booking/admin_rejection.html',context)


def admin_disapproved(request):
    queryset = Booking.objects.all().order_by('booked_date').filter(status__iexact="Disapproved")
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }
    if request.method == 'POST':
        if form['booked_date'] =="":
            return redirect('view_user')
        else:
            queryset = Booking.objects.all().order_by('booked_date').filter(booked_date__icontains=form['booked_date'].value()).filter(status__iexact="Disapproved")
            context = {
                "queryset" : queryset,
                "form" : form,
            }
    return render(request,'booking/admin_disapproved.html',context)





def approved(request):
    return render(request,'booking/approved.html')

def rejected(request):
    return render(request,'booking/rejected.html')
    
def pending(request):
    return render(request,'booking/pending.html')


def auto_rejected(request):

    user = Hygiene.objects.all().filter(status="High Risk")
    if request.method == 'POST':
        book = Booking.objects.all().filter(user_id=request.user)
    context = {"user" : user}
    return render(request,'booking/auto_rejected.html',context)





