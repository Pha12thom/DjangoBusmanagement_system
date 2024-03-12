from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm,  SearchForm, BookingForm

from django.contrib.auth.models import User
from .models import Route, Bus, UserProfile,  Schedule, Ticket



def homepage(request):
    return render(request, 'h.html')

def home(request):
    return render(request, 'home.html')

#register
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')    
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

 

def login(request): 
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User = authenticate(request, username=username, password=password)
            if User is not None:
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def search_routes(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            departure_city = form.cleaned_data['departure_city']
            arrival_city = form.cleaned_data['arrival_city']
            departure_time = form.cleaned_data['departure_time']
            matching_routes = Route.objects.filter(
                departure_time = departure_time,
                departure_city=departure_city,
                arrival_city=arrival_city
            )
            return render(request, 'route_list.html', {'routes': matching_routes})
    else:
        form = SearchForm()    
    return render(request, 'search.html', {'form': form})



#1 search
def search_form(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            departureTown = form.cleaned_data['departure_city']
            arrivalTown = form.cleaned_data['arrival_city']    
            departureTime = form.cleaned_data['departure_time']
            matching_buses = Bus.objects.filter(departure_city=departureTown, arrival_city=arrivalTown, departure_time=departureTime)
            return render(request, 'search_results.html', {'matching_buses': matching_buses})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})



def booking(request, id):
    schedule = Schedule.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.schedule = schedule  
            return redirect('booking_success') 
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form, 'schedule': schedule})

def print_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket.html', {'ticket': ticket})