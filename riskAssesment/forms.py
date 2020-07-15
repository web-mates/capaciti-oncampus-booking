from django import forms
from django.db import models
from riskAssesment.models import  Symptoms,Travel,Hygiene,Screening




   

class SymptomsForm(forms.ModelForm):
     
    class Meta:
        widgets = { 'caugh': forms.RadioSelect,
                    'shortness_of_breath': forms.RadioSelect,
                    'fever': forms.RadioSelect,
                    'body_pain': forms.RadioSelect,
                    'sore_throat': forms.RadioSelect,
                    'loss_of_taste': forms.RadioSelect,
                    'loss_of_smell': forms.RadioSelect,
        
        }
        model = Symptoms
        fields = [

            'caugh', 
            'shortness_of_breath', 
            'fever', 
            'body_pain', 
            'sore_throat', 
            'loss_of_taste', 
            'loss_of_smell',
            'status', 
      
        ]


class TravelForm(forms.ModelForm):

    class Meta:
        widgets = { 'transport': forms.RadioSelect,
                    'travell_locally_past_21dys': forms.RadioSelect,
                    'gathering_with_moreThan_10': forms.RadioSelect,
                    'contact_with_person_covid_positive': forms.RadioSelect,
         
        }
        model = Travel
        fields = [

            
            'transport',
            'travell_locally_past_21dys',
            'gathering_with_moreThan_10', 
            'contact_with_person_covid_positive',
            'status',
           
            


        ]

class HygieneForm(forms.ModelForm):

    class Meta:
        widgets = { 'medical_condition_risk_to_covid': forms.RadioSelect,
                    'medical_condition_in_family': forms.RadioSelect,
                    'understand_social_distancing': forms.RadioSelect,
                    'wear_mask': forms.RadioSelect,
                    'practice_safe_hygene': forms.RadioSelect,
                    'terms_and_conditions': forms.CheckboxInput,
        
        
        }
        model = Hygiene
        fields = [
           
            'medical_condition_risk_to_covid',
            'medical_condition_in_family', 
            'understand_social_distancing',
            'wear_mask', 
            'practice_safe_hygene', 
            'terms_and_conditions',
            'status',
            'comment',
         
        ]



class ScreeningForm(forms.ModelForm):

    class Meta:
        widgets = {
                    'caugh': forms.RadioSelect,
                    'shortness_of_breath': forms.RadioSelect,
                    'fever': forms.RadioSelect,
                    'body_pain': forms.RadioSelect,
                    'sore_throat': forms.RadioSelect,
                    'loss_of_taste': forms.RadioSelect,
                    'loss_of_smell': forms.RadioSelect,
                    'transport': forms.RadioSelect,
                    'travell_locally_past_21dys': forms.RadioSelect,
                    'gathering_with_moreThan_10': forms.RadioSelect,
                    'contact_with_person_covid_positive': forms.RadioSelect,
                    'medical_condition_risk_to_covid': forms.RadioSelect,
                    'medical_condition_in_family': forms.RadioSelect,
                    'understand_social_distancing': forms.RadioSelect,
                    'wear_mask': forms.RadioSelect,
                    'practice_safe_hygene': forms.RadioSelect,
                    'terms_and_conditions': forms.CheckboxInput,
        
        
        }
        model = Screening
        fields = [
            'caugh', 
            'shortness_of_breath', 
            'fever', 
            'body_pain', 
            'sore_throat', 
            'loss_of_taste', 
            'loss_of_smell',
            'status',
            'transport',
            'travell_locally_past_21dys',
            'gathering_with_moreThan_10', 
            'contact_with_person_covid_positive',
            'medical_condition_risk_to_covid',
            'medical_condition_in_family', 
            'understand_social_distancing',
            'wear_mask', 
            'practice_safe_hygene', 
            'terms_and_conditions',
            'status',
            'comment',
         
        ]



        
     
