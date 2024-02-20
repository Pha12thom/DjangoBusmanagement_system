# Import the Bus model
from managements.models import Bus

# Create a new Bus object
bus1 = Bus.objects.create(
    name='Your Bus Name',
    color='Bus Color',
    no_plate='Bus Number Plate',
    seats=50  
)
bus1.save()
