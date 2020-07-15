from django.shortcuts import render
from riskAssesment.models import Symptoms, Hygiene, Travel,Screening
from .forms import SymptomsForm,TravelForm,HygieneForm,ScreeningForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def symptoms_view(request):

    form = SymptomsForm()

    if request.method == 'POST':

        form = SymptomsForm(request.POST)
        if form.is_valid():

            instance = form.save(commit = False)
            if  (instance.caugh == "Yes" and instance.shortness_of_breath == "Yes") or (instance.caugh == "Yes" and instance.fever == "Yes") or (instance.caugh == "Yes" and instance.body_pain == "Yes") or (instance.caugh == "Yes" and instance.sore_throat == "Yes" ) or (instance.caugh == "Yes" and instance.loss_of_taste == "Yes") or (instance.caugh == "Yes" and instance.loss_of_smell == "Yes")  :
                instance.status = "High Risk"

            elif (instance.shortness_of_breath == "Yes" and instance.fever == "Yes") or (instance.shortness_of_breath == "Yes" and instance.body_pain == "Yes") or (instance.shortness_of_breath == "Yes" and instance.sore_throat == "Yes")  or (instance.shortness_of_breath == "Yes" and instance.loss_of_taste == "Yes") or (instance.shortness_of_breath == "Yes" and instance.loss_of_smell == "Yes")  :
                instance.status = "High Risk"

            elif   (instance.fever == "Yes" and instance.body_pain == "Yes") or (instance.fever == "Yes" and instance.sore_throat == "Yes")  or (instance.fever == "Yes" and  instance.loss_of_taste == "Yes") or (instance.fever == "Yes" and instance.loss_of_smell == "Yes")  :
                instance.status = "High Risk"

            elif   (instance.body_pain == "Yes" and instance.sore_throat == "Yes" ) or (instance.body_pain == "Yes" and  instance.loss_of_taste == "Yes") or (instance.body_pain == "Yes" and instance.loss_of_smell == "Yes" ) :
                instance.status = "High Risk"
            elif   (instance.sore_throat == "Yes"  and instance.loss_of_taste == "Yes") or (instance.sore_throat == "Yes"  and instance.loss_of_smell == "Yes")  :
                instance.status = "High Risk"

            elif  instance.caugh == "Yes" or instance.shortness_of_breath == "Yes" or instance.fever == "Yes" or instance.body_pain == "Yes" or instance.sore_throat == "Yes"  or instance.loss_of_taste == "Yes" or instance.loss_of_smell == "Yes"  :
                instance.status = "Low Risk"

            else:
                instance.status = 'Normal'
            
            instance.user = request.user
            instance.save()
            return redirect('travel') 
        
    context = {'form':form}
       
    return render(request,'riskAssesment/symptoms.html',context)


def travel_view(request):

    form = TravelForm()

    if request.method == 'POST':

        form = TravelForm(request.POST)
        if form.is_valid():

            instance = form.save(commit = False)
            if instance.contact_with_person_covid_positive == "Yes":
                instance.status = "High Risk"
            elif instance.travell_locally_past_21dys == "Yes" or instance.gathering_with_moreThan_10 =="Yes":
                instance.status = "Low Risk"
            else:
                instance.status = 'Normal'

            instance.user = request.user
            instance.save()
            return redirect('hygiene') 
        
    context = {'form':form}
       
    return render(request,'riskAssesment/travel.html',context)

def hygiene_view(request):

    form = HygieneForm()
    form2 =  ScreeningForm()
    if request.method == 'POST':

        form = HygieneForm(request.POST)
        form2 = ScreeningForm(request.POST)

        if form.is_valid() or form2.is_valid():
            
            instance = form.save(commit = False)
            screening = form2.save(commit = False)

           
            symptoms = Symptoms.objects.latest("user_id")
            travel = Travel.objects.latest("user_id")

            screening.caugh = symptoms.caugh 
            screening.shortness_of_breath = symptoms.shortness_of_breath 
            screening.fever = symptoms.fever 
            screening.body_pain = symptoms.body_pain 
            screening.sore_throat = symptoms.sore_throat 
            screening.loss_of_taste = symptoms.loss_of_taste
            screening.loss_of_smell = symptoms.loss_of_smell
            screening.transport = travel.transport
            screening.travell_locally_past_21dys = travel.travell_locally_past_21dys
            screening.gathering_with_moreThan_10 = travel.gathering_with_moreThan_10 
            screening.contact_with_person_covid_positive = travel.contact_with_person_covid_positive
            screening.medical_condition_risk_to_covid = instance.medical_condition_risk_to_covid
            screening.medical_condition_in_family = instance.medical_condition_in_family 
            screening.understand_social_distancing = instance.understand_social_distancing
            screening.wear_mask= instance.wear_mask 
            screening.practice_safe_hygene = instance.practice_safe_hygene 
            screening.terms_and_conditions = instance.terms_and_conditions
            screening.status = instance.status
            screening.comment = instance.comment
            screening.user = request.user
            screening.save()



            if instance.medical_condition_risk_to_covid =="Yes" or instance.medical_condition_in_family == "Yes" or instance.understand_social_distancing == "No" or instance.wear_mask == "No" or instance.practice_safe_hygene == "No":
                instance.status = "Low Risk"
            elif instance.medical_condition_risk_to_covid =="Yes" and instance.medical_condition_in_family == "Yes" and instance.understand_social_distancing == "No" and instance.wear_mask == "No" and instance.practice_safe_hygene == "No":
                instance.status = "High Risk"   
                  
            elif instance.medical_condition_risk_to_covid =="Yes" or instance.medical_condition_in_family == "Yes" and (instance.understand_social_distancing == "No" or instance.wear_mask == "No" or instance.practice_safe_hygene == "No"):
                instance.status = "High Risk" 
            else:
                instance.status = "Normal"

            symptoms = Symptoms.objects.latest("user_id")
            travel = Travel.objects.latest("user_id")
            screening = Screening.objects.latest("user_id")
                


            if symptoms.status =="High Risk"  or travel.status =="High Risk" :
                instance.status = "High Risk" 
                instance.user = request.user
                instance.Screening_id = screening.id
                instance.save()
                return redirect('rejected')

            elif travel.status =="Low Risk" and (instance.medical_condition_risk_to_covid =="Yes" or instance.medical_condition_in_family == "Yes" or instance.understand_social_distancing == "No" or instance.wear_mask == "No" or instance.practice_safe_hygene == "No"):
                return redirect('rejected')
            
            elif travel.status =="Low Risk" and symptoms.status == "Low Risk":
                return redirect('rejected')
            else:
                instance.user = request.user
                instance.Screening_id = screening.id
                instance.save()
                return redirect('booking') 


           
        
    context = {'form':form,
               'form2':form2,
    }
       
    return render(request,'riskAssesment/hygiene.html',context)



