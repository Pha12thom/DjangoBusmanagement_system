from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm,  SearchForm
from django.contrib.auth.models import User
from .models import Route, Bus





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




#3 search
def bus_detail(request):
    buses = Bus.objects.all()
    context = {
        'Bus': buses
    }
    return render(request, 'bus_detail.html', context)
"""
#2 search
def search(request):
    if request.method == 'POST':
        form = BusSearchForm(request.POST)
        if form.is_valid():
            search_date = form.cleaned_data['search_date']
            Searched_bus = Testing.objects.filter(departure_date=search_date)
            return render(request, 'bus_search.html', {'searched_bus': Searched_bus})
    else:
        form = BusSearchForm()
        return render(request, 'bus_form.html', {'form': form})
    

def bus_search(request):
    if request.method == 'POST':
        form = BusForm()
        if form.is_valid():
            cityFrom = form.cleaned_data['from_city']
            cityTo = form.cleaned_data['to_city']
            searchDate= form.cleaned_data['search_date']
            
            matching_buses = Bus.objects.filter(departure_city=cityFrom, arrival_city=cityTo, departure_time=searchDate)
            return render(request, 'final_results.html', {'matching_buses': matching_buses})
    else:
        form = SearchForm()
    return render(request, 'final_form.html', {'form': form})

"""  
    