from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Ticket, CITIES_GROUPS, CITIES, Bus

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'firstname', 'secondName', 'email']
        

class PaymentForm(forms.Form):
    payment_method = forms.CharField(max_length=100)
    transaction_id = forms.CharField(max_length=100)
    amount = forms.DecimalField(max_digits=8, decimal_places=2)



class BookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['schedule', 'seat_no', 'passenger_name', 'passengerAge', 'gender']


class SearchForm(forms.Form):
    departure_city=  forms.ChoiceField(choices=CITIES)
    arrival_city=  forms.ChoiceField(choices=CITIES)
    departure_time = forms.DateField(
        label='Departure Date',
        input_formats=["%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y"],
        widget=forms.DateInput(attrs={'type': 'date'})
        )

from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['schedule', 'seat_no', 'passenger_name', 'passengerAge', 'gender']

"""
class BusSearchForm(forms.Form):
    search_date = forms.DateField(label='Search Date')
    

class BusForm(forms.Form):
    search_date = forms.DateField(label='Search Date: yyyy-mm-dd')
    from_city = forms.CharField(max_length=150, label='From City')
    to_city = forms.CharField(max_length=150, label='To city')
"""
