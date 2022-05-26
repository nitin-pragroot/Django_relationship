from django.db import models

#Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
    
    
class User(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Page(models.Model):
    page_name = models.CharField(max_length=255)
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.page_name
    
    
class Worker(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ManyToManyField( Worker)
    
    def __str__(self):
        return self.name
    