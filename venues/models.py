from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_name = models.CharField(max_length=128)
