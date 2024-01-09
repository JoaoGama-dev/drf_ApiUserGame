from django.db import models

class Games(models.Model):
    name = models.CharField(max_length=250)

def __str__(self):
    return self.name

class User(models.Model):
    name = models.CharField(max_length=250)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)

def __str__(self):
    return self.name

