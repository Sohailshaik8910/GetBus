from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Buses(models.Model):
    Bus_Name = models.CharField(max_length=100)
    From = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    Price = models.PositiveIntegerField()
    Date = models.DateField()
    Bus_Type = models.CharField(max_length=100, default="AC")


class Ticket(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Bus = models.ForeignKey(Buses, on_delete=models.CASCADE, default=None)
    Name = models.CharField(max_length=100)
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length=100)
    Ticket_No = models.PositiveIntegerField(default=0)


class Passenger(models.Model):
    P_Name = models.CharField(max_length=100, default=None)
    Age = models.PositiveIntegerField(default=0)
    Gender = models.CharField(max_length=100, default=None)
    Bus_id = models.ForeignKey(Buses, on_delete= models.CASCADE, default=None)


