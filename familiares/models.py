from django.db import models

# Create your models here.
class Familiares(models.Model):
    """Main class of the Familiares app"""
    name=models.CharField(max_length=100)
    age=models.FloatField()
    is_lotr_fan=models.BooleanField()
