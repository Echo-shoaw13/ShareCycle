from django.db import models

# Create your models here.

class Bike(models.Model):
    BikeId = models.AutoField(primary_key=True)
    BikeState = models.BooleanField()
    BikeType = models.CharField(max_length=64)
    Location = models.CharField(max_length=128)
    Condition = models.CharField(max_length=64)

class Order(models.Model):
    OrderId = models.AutoField(primary_key=True)
    BikeId = models.IntegerField()
    UserId = models.IntegerField()
    StartLocation = models.CharField(max_length=128)
    EndLocation = models.CharField(max_length=128)
    StartTime = models.DateTimeField(auto_now_add=True)
    EndTime = models.DateTimeField()
    Bill = models.FloatField()
    OrderState = models.BooleanField()

class Account(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=64)
    Password = models.CharField(max_length=128)
    Role = models.CharField(max_length=64)
    Email = models.EmailField()
    Wallet = models.FloatField()
    Owed = models.FloatField()

