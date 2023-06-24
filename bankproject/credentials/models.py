from django.db import models

# Create your models here.
from django.db import models

# class Country(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     name = models.CharField(max_length=100)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

class Application(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DOB = models.DateField()
    Age = models.IntegerField()
    phonenumber = models.IntegerField()
    email = models.EmailField()
    Address=models.TextField()

    def __str__(self):
        return self.name
