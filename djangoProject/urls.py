"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import (register,loginPage,logout_user,users,edit_user,delete,view_user,history,
                            screening,approve_group,disapprove_group,reject_group,
                            approve_reject_group,approve_disapproved_group,
                            home,book_now,aboutus,screening_approved,
                            screening_auto_reject,screening_rejected,screening_disapproved
)
from booking.views import booking_view,admin_view,approved,rejected,pending,admin_pending,admin_approved,admin_rejection,admin_disapproved,auto_rejected
from riskAssesment.views import symptoms_view,travel_view,hygiene_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register, name ='register'),
    path('', loginPage, name ='login'),
    path('users/',users, name ='users'),
    path('logout_user/', logout_user, name ='logout_user'),
    path('symptoms/',symptoms_view, name ='symptoms'),
    path('travel/',travel_view, name ='travel'),
    path('hygiene/',hygiene_view, name ='hygiene'),
    path('booking/',booking_view, name ='booking'),
    path('admin_page/',admin_view, name ='admin_page'),
    path('edit/<int:id>', edit_user, name ='edit'),
    path('delete/<int:id>', delete, name ='delete'),
    path('view_user/<int:id>', view_user, name ='view_user'),
    path('approved/',approved, name ='approved'),
    path('history/',history, name ='history'),
    path('rejected/',rejected, name ='rejected'),
    path('pending/',pending, name ='pending'),
    path('admin_pending/',admin_pending, name ='admin_pending'),
    path('admin_approved/',admin_approved, name ='admin_approved'),
    path('admin_rejection/',admin_rejection, name ='admin_rejection'),
    path('admin_disapproved/',admin_disapproved, name ='admin_disapproved'),
    path('screening/<int:id>',screening, name ='screening'),
    path('screening_approved/<int:id>',screening_approved, name ='screening_approved'),
    path('screening_auto_reject/<int:id>',screening_auto_reject, name ='screening_auto_reject'),
    path('screening_rejected/<int:id>',screening_rejected, name ='screening_rejected'),
    path('screening_disapproved/<int:id>',screening_disapproved, name ='screening_disapproved'),
    path('approve_group/<int:id>',approve_group, name ='approve_group'),
    path('disapprove_group/<int:id>',disapprove_group, name ='disapprove_group'),
    path('reject_group/<int:id>',reject_group, name ='reject_group'),
    path('approve_reject_group/<int:id>',approve_reject_group, name ='approve_reject_group'),
    path('approve_disapproved_group/<int:id>',approve_disapproved_group, name ='approve_disapproved_group'),
    path('auto_rejected/',auto_rejected, name ='auto_rejected'),
    path('home/',home, name ='home'),
    path('book_now/',book_now, name ='book_now'),
    path('aboutus/',aboutus, name ='aboutus'),
  



]
