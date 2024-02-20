from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from .forms import SearchForm
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
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
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
            departure_date = form.cleaned_data['departure_date']
            
            # Perform query to get matching routes
            matching_routes = Route.objects.filter(
                departure_city__icontains=departure_city,
                arrival_city__icontains=arrival_city
            )
            # You can also filter routes based on departure date if needed
            
            return render(request, 'route_list.html', {'routes': matching_routes})
    else:
        form = SearchForm()
    
    return render(request, 'search.html', {'form': form})




def search_form(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Process the form data
            departure_city = form.cleaned_data['departure_city']
            arrival_city = form.cleaned_data['arrival_city']
            departure_date = form.cleaned_data['departure_date']
            # Perform database query based on the search criteria
            matching_routes = Route.objects.filter(departure_city=departure_city, arrival_city=arrival_city)
            return render(request, 'search_results.html', {'routes': matching_routes})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})


def bus_detail(request):
    buses = Bus.objects.all()
    context = {
        'Bus': buses
    }
    return render(request, 'bus_detail.html', context)
