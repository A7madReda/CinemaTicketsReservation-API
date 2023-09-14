from django.db import models

class Movie(models.Model):
        hall = models.CharField(max_length=10)
        name = models.CharField(max_length=50)
        date = models.DateField()
        

class Guest(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    

class Reservition(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservition', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservition', on_delete=models.CASCADE)
