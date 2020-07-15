from django import forms
from .models import Booking
from datetime import datetime,date




class DateInput(forms.DateInput):
    input_type = 'date'


class BookingCreateForm(forms.ModelForm):
    
    
    class Meta:
        widgets ={'booked_date': DateInput()}
        model = Booking
        fields = [
            'booked_date',
            'user',
            'status',
            ]

class CandidateSearchForm(forms.ModelForm):
    
    class Meta:
        widgets ={'booked_date': DateInput()}
        model = Booking
        fields = [
            'booked_date',
            ]