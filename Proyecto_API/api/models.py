from django.db import models

# Create your models here.

# Modelo de Company

class Company(models.Model):
    name=models.CharField(max_length=50)
    website=models.URLField(max_length=100)
    foundation=models.PositiveIntegerField()
