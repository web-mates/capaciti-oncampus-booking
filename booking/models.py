from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime,date
from django.contrib.auth.models import User
from riskAssesment.models import Screening


class Booking(models.Model):

    user = models.ForeignKey(User ,on_delete=models.CASCADE,blank =True)
    booked_date = models.DateField(blank =True, default = date.today())
    status = models.CharField(max_length=250 ,blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    Screening = models.ForeignKey(Screening ,on_delete=models.CASCADE,blank =True)





    

