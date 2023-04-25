from django.db import models

class Vehicle(models.Model):
    name=models.CharField(max_length=250)
    model=models.CharField(max_length=200)
    category=models.CharField(max_length=230)
    fuel_type=models.CharField(max_length=240)
    kms=models.CharField(max_length=260)
    number=models.CharField(max_length=230,unique=True)
    description=models.CharField(max_length=2000)
    owner_type=models.CharField(max_length=250)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name



class Mobiles(models.Model):
    name=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    display=models.CharField(max_length=200,default="lcd")
    def __str__(self):
        return self.name
    

class Movies(models.Model):
    name=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    rate=models.PositiveIntegerField()
    language=models.CharField(max_length=200)
    def __str__(self):
        return self.name