from django.db import models
from django import forms
from django.contrib.auth.models import User


class choices(models.Model):
    names= models.Choices

CITIES_GROUPS = [
    ('Nairobi', 'Kisumu', 'Mombasa','Nakuru'),
    ('Siaya', 'Meru', 'Kisii'),
    ('Narok', 'Nyeri'),
    ('Thika',  'Turkana' ),
]
CITIES = [(city, city) for group in CITIES_GROUPS for city in group ]

class Bus(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    no_plate = models.CharField(max_length=150)
    seats = models.IntegerField()
    departure_city = models.CharField(max_length=150, choices=CITIES)
    arrival_city = models.CharField(max_length=100, null=True, choices=CITIES)
    departure_time = models.DateTimeField()  # Updated field to use DateTimeField
    depart_time = models.TimeField(null=True)
    
    def __str__(self):
        return f"{self.name }  {self.no_plate} {self.seats} {self.departure_city} {self.departure_time}"
    
class Route(models.Model):
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=150)
    distance = models.FloatField() 
    timeTaken = models.DurationField()
    buses = models.ManyToManyField(Bus, related_name='routes')  # Many-to-many relationship with Bus model



#schedule model 
class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departTime=models.DateTimeField()
    arrivalTime = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    route = models.ForeignKey(Route, on_delete= models.CASCADE)


#Ticket model 
class Ticket(models.Model):
    schedule=models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat_no = models.CharField(max_length=50)
    passenger_name =models.CharField(max_length=100)
    passengerAge= models.IntegerField()
    gender=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
        

#payment model   
class Payment(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    paymentMethod = models.CharField(max_length=100)
    transactionId= models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8, decimal_places=2)
    

#user profile
class UserProfile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length= 15)
    booking_history = models.ManyToManyField(Ticket, blank=True)
    firstname = models.CharField(max_length= 100)
    secondName = models.CharField(max_length=100)
    email= models.CharField(max_length=200)


class Testing(models.Model):
    departure_date = models.DateField()
    No_of_seats = models.IntegerField()
    license = models.CharField(max_length=100)
    name = models.CharField(max_length= 100)
    
CITIES_GROUPS = [
    ('Nairobi', 'Kisumu', 'Mombasa','Nakuru'),
    ('Siaya', 'Meru', 'Kisii', 'Bungoma'),
    ('Narok', 'Nyeri', 'Migori', 'Busia'),
    ('Thika',  'Turkana', 'Kitengela'),
]

CITIES = [(city, city) for group in CITIES_GROUPS for city in group ]

