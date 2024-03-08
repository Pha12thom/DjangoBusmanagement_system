from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm,  SearchForm
from django.contrib.auth.models import User
from .models import Route, Bus, UserProfile





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

# In your views.py
from django.shortcuts import render, get_object_or_404
from .models import Bus

def bus_detail(request, bus_id):
    bus = get_object_or_404(Bus, pk=bus_id)
    return render(request, 'bus_detail.html', {'bus': bus})




def seat_selection(request):
    seats = range(1, 13)
    return render(request, 'selection.html', {'seats': seats})



def book_seat(request, seat_number):
    if request.method == 'POST':
    
        customer_name = request.POST.get('customer_name')
        price = request.POST.get('price')
        booking_date = request.POST.get('booking_date')
        
        # Save booking details to the database
        booking = Booking.objects.create(
            customer_name=customer_name,
            seat_number=seat_number,
            price=price,
            booking_date=booking_date
        )
        
        return redirect('confirm_booking', seat_number=seat_number)
    return render(request, 'seat.html', {'seat_number': seat_number})





def confirm_booking(request, seat_number): 
    booking = Booking.objects.get(seat_number=seat_number)
    return render(request, 'booking.html', {'booking': booking})

    
