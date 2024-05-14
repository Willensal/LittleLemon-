from django.db import models

# Create your models here.

class Booking(models.Model):
    ID = models.IntegerField()
    Name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField()
    BookingDate = models.DateTimeField()
    
class Menu(models.Model):
    ID = models.IntegerField()
    Title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.IntegerField()