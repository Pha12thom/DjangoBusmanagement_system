from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm,  SearchForm, BookingForm, TicketForm, PrintTicketForm
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



def print_ticket(request):
    if request.method == 'POST':
        form = PrintTicketForm(request.POST)
        if form.is_valid():
            ticket_id = form.cleaned_data['ticket_id']
            try:
                ticket = Ticket.objects.get(id=ticket_id)
                return render(request, 'print_ticket.html', {'ticket': ticket})
            except Ticket.DoesNotExist:
                return HttpResponse('Ticket not found')
    else:
        form = PrintTicketForm()
    return render(request, 'print_ticket_form.html', {'form': form})




def book_ticket(request, schedule_id):
    schedule = Schedule.objects.get(id=schedule_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            passenger_name = form.cleaned_data['passenger_name']
            passenger_age = form.cleaned_data['passenger_age']
            gender = form.cleaned_data['gender']
            payment_method = form.cleaned_data['payment_method']

            ticket = Ticket.objects.create(
                schedule=schedule,
                passenger_name=passenger_name,
                passengerAge=passenger_age,
                gender=gender,
                user=request.user,
                pay=payment_method
            )

            # Assuming payment processing here, create a payment object
            # payment = Payment.objects.create(ticket=ticket, ...)

            # Redirect to a page where the user can print their ticket
            return redirect('print_ticket', ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(request, 'book_ticket.html', {'form': form, 'schedule': schedule})


from django.contrib.auth.decorators import login_required

@login_required
def save_ticket(request):
    if request.method == 'POST':
        schedule_id = request.POST.get('schedule')
        seat_no = request.POST.get('seat_no')
        passenger_name = request.POST.get('passenger_name')
        passenger_age = request.POST.get('passengerAge')
        gender = request.POST.get('gender')
        pay = request.POST.get('paying.pay')
        schedule = Schedule.objects.get(id=schedule_id)
        user = request.user  # Get the authenticated user
        
        # Create a new Ticket object and save it to the database
        ticket = Ticket.objects.create(
            schedule=schedule,
            seat_no=seat_no,
            passenger_name=passenger_name,
            passengerAge=passenger_age,
            gender=gender,
            user=user,  # Assign the authenticated user
            pay=pay
        )
        # Redirect the user to the ticket confirmation page
        return redirect('ticket_confirmation')
    # Fetch schedules to display in the form
    schedules = Schedule.objects.all()
    pays = Ticket.objects.all()
    return render(request, 'ticket_form.html', {'schedules': schedules, 'pays': pays})


def ticket_confirmation(request):
    # Fetch the last ticket added to the database
    last_ticket = Ticket.objects.order_by('-id').first()
    if last_ticket:
        return render(request, 'ticket_confirmation.html', {'ticket': last_ticket})
    else:
        
        
        # Handle case where there are no tickets in the database
        return render(request, 'ticket_confirmation.html', {'ticket': None})

