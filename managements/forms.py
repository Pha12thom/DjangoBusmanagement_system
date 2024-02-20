from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Ticket

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
    departure_city = forms.CharField(max_length=100)
    arrival_city = forms.CharField(max_length=100)
    departure_date = forms.DateField()
