from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
from django import forms
from django.core.exceptions import ValidationError




TRANSPORT =[

     ('Car', 'Car'), ('Public', 'Public'),
]

CHOICE =[
          
  

     ('Yes', 'Yes'), ('No', 'No'),
]

def validate(value):


     if  value == 'Car' or  value == 'Public':

          return value 
     elif value == 'Yes' or value == 'No':
          return value



class Symptoms(models.Model):

   
    caugh= models.CharField( max_length=50, choices=CHOICE,default="")
    shortness_of_breath = models.CharField( max_length=50, choices=CHOICE,default="")
    fever =  models.CharField( max_length=50, choices=CHOICE,default="")
    body_pain =  models.CharField( max_length=50, choices=CHOICE,default="")
    sore_throat =  models.CharField( max_length=50, choices=CHOICE,default="")
    loss_of_taste =  models.CharField( max_length=50, choices=CHOICE,default="")
    loss_of_smell =  models.CharField( max_length=50, choices=CHOICE,default="")
    date= models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,blank =True)
    user = models.ForeignKey(User ,on_delete=models.CASCADE,blank =True)

class Travel(models.Model):

     transport = models.CharField( max_length=50, choices=TRANSPORT,default="")
     travell_locally_past_21dys = models.CharField( max_length=50, choices=CHOICE,default="")
     gathering_with_moreThan_10 =models.CharField( max_length=50, choices=CHOICE,default="")
     contact_with_person_covid_positive =models.CharField( max_length=50, choices=CHOICE,default="")
     date= models.DateField(auto_now_add=True)
     status = models.CharField(max_length=50,blank =True)
     user = models.ForeignKey(User ,on_delete=models.CASCADE,blank =True)



class Screening(models.Model):


     caugh= models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     shortness_of_breath = models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     fever =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     body_pain =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     sore_throat =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     loss_of_taste =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     loss_of_smell =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     transport = models.CharField( max_length=50, choices=TRANSPORT,default="",blank =True)
     travell_locally_past_21dys = models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     gathering_with_moreThan_10 =models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     contact_with_person_covid_positive =models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     medical_condition_risk_to_covid =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     medical_condition_in_family =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     understand_social_distancing =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     wear_mask =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     practice_safe_hygene =  models.CharField( max_length=50, choices=CHOICE,default="",blank =True)
     terms_and_conditions =  models.CharField( max_length=50,blank =True)
     date= models.DateField(auto_now_add=True)
     status = models.CharField(max_length=50,blank =True)
     comment = models.TextField(max_length=250,default="",blank=True)
     user = models.ForeignKey(User ,on_delete=models.CASCADE,blank =True)


class Hygiene(models.Model):
     medical_condition_risk_to_covid =  models.CharField( max_length=50, choices=CHOICE,default="")
     medical_condition_in_family =  models.CharField( max_length=50, choices=CHOICE,default="")
     understand_social_distancing =  models.CharField( max_length=50, choices=CHOICE,default="")
     wear_mask =  models.CharField( max_length=50, choices=CHOICE,default="")
     practice_safe_hygene =  models.CharField( max_length=50, choices=CHOICE,default="")
     terms_and_conditions =  models.CharField( max_length=50)
     date= models.DateField(auto_now_add=True)
     status = models.CharField(max_length=50,blank =True)
     comment = models.TextField(max_length=250,default="",blank=True)
     user = models.ForeignKey(User ,on_delete=models.CASCADE,blank =True)
     Screening = models.ForeignKey(Screening ,on_delete=models.CASCADE,blank =True)
     



