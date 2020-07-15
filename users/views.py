from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CreateUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import EditUserForm
from booking.models import Booking
from booking.forms import BookingCreateForm, CandidateSearchForm
from riskAssesment.models import Symptoms, Hygiene, Travel,Screening
from riskAssesment.forms import SymptomsForm, TravelForm, HygieneForm,ScreeningForm

def users(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request,'users/users.html',context)

def register(request):

    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUser()

        if request.method == 'POST':
            form = CreateUser(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was successfully created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request,'users/register.html',context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('symptoms')
    else:

        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(email=email).exists():
                username = User.objects.get(email=email.lower()).username
                user = authenticate(username=username, password=password)

                if user is not None :
                    if user.is_superuser == 1:
                        login(request,user)
                        return redirect('admin_page')
                    elif user.is_superuser ==0:
                        login(request,user)
                        return redirect('home')
                else:
                    messages.success(request, 'Username or Password is incorrect' )
            else:
                messages.success(request, 'Account does not exist or removed from the system.' )


        context = {}
        return render(request,'users/login.html',context)



def users_view_page(request):

   user = User.objects.all()
   context = {'user': user}
   return render(request,'users/users.html',context)


def edit_user(request, id):

    form = EditUserForm()
    user = User.objects.get(id=id)


    if request.method == 'POST':
        form = EditUserForm(request.POST, instance = user)

        if form.is_valid():

            user_form =form.save()
            custom_form = user.save(False)
            custom_form= user_form
            custom_form.save()
            return redirect('users')


    context = {'form': form,
        }
    return render(request,'users/edit.html',context)






def logout_user(request):
    logout(request)
    return redirect('login')


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')


def view_user(request, id):

    user = User.objects.get(id=id)
    book = Booking.objects.all().filter(user_id=user)
    form = CandidateSearchForm(request.POST or None)
    context = {
        "form" : form,
        'book' : book,
    }

    if request.method == 'POST':
        if form['booked_date'] =="":
            return redirect('view_user')
        else:
            user = User.objects.get(id=id)
            book = Booking.objects.all().filter(booked_date__icontains=form['booked_date'].value()).filter(user_id=user)
            context = {
                "book" : book,
                "form" : form,
            }

    return render(request,'users/view_user.html',context)


def history(request):

    book = Booking.objects.all().filter(user_id=request.user)
    if request.method == 'POST':
        book = Booking.objects.all().filter(user_id=request.user)
    context = {"book" : book}

    return render(request,'users/history.html',context)


def screening(request,id):

    user = Booking.objects.get(id=id)
    queryset = Screening.objects.all().filter(id=user.Screening_id) 
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }

    return render(request,'users/screening.html',context)



def screening_approved(request,id):

    user = Booking.objects.get(id=id)
    queryset = Screening.objects.all().filter(id=user.Screening_id) 
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }

    return render(request,'users/screening_approved.html',context)


def screening_auto_reject(request,id):

    user = Hygiene.objects.get(id=id)
    queryset = Screening.objects.all().filter(id=user.Screening_id) 
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }

    return render(request,'users/screening_auto_reject.html',context)

def screening_rejected(request,id):

    user = Booking.objects.get(id=id)
    queryset = Screening.objects.all().filter(id=user.Screening_id) 
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }

    return render(request,'users/screening_rejected.html',context)


def screening_disapproved(request,id):

    user = Booking.objects.get(id=id)
    queryset = Screening.objects.all().filter(id=user.Screening_id) 
    form = CandidateSearchForm(request.POST or None)
    context = {
        "queryset" : queryset,
        "form" : form,
    }

    return render(request,'users/screening_disapproved.html',context)



def approve_group(request, id):

    user = Booking.objects.get(id=id)
    book = Booking.objects.get(id=user.id)
    book.status = "Approved"
    book.save()
    return redirect('admin_pending')

def disapprove_group(request, id):

    user = Booking.objects.get(id=id)
    book = Booking.objects.get(id=user.id)
    book.status = "Disapproved"
    book.save()
    return redirect('admin_approved')


def reject_group(request, id):

    user = Booking.objects.get(id=id)
    book = Booking.objects.get(id=user.id)
    book.status = "Rejected"
    book.save()
    return redirect('admin_pending')

def approve_reject_group(request, id):

    user = Booking.objects.get(id=id)
    book = Booking.objects.get(id=user.id)
    book.status = "Approved"
    book.save()
    return redirect('admin_rejection')

def approve_disapproved_group(request, id):

    user = Booking.objects.get(id=id)
    book = Booking.objects.get(id=user.id)
    book.status = "Approved"
    book.save()
    return redirect('admin_disapproved')

def home(request):
    context = {}
    return render(request,'users/home.html',context)

def book_now(request):
    context = {}
    return redirect('symptoms')

@ login_required(login_url ='login')
def aboutus(request):
    context = {}
    return render(request,'users/aboutus.html',context)








