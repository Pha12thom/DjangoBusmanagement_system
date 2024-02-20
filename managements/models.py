from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
#bus model
class Bus(models.Model):
    name= models.CharField(max_length=150)
    color= models.CharField(max_length=150)
    no_plate=models.CharField(max_length=150)
    seats=models.IntegerField()
    def __str__(self):
        return self.name
    


#route model 
class Route(models.Model):
    departure_city = models.CharField(max_length=100)
    arrival_city= models.CharField(max_length=150)
    distance=models.FloatField()
    timeTaken=models.DurationField()
    
"""
class Bus(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    no_plate = models.CharField(max_length=150)
    seats = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Route(models.Model):
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=150)
    distance = models.FloatField()
    timeTaken = models.DurationField()
    buses = models.ManyToManyField(Bus, related_name='routes')  # Many-to-many relationship with Bus model

    def __str__(self):
        return f"{self.departure_city} to {self.arrival_city}"


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

