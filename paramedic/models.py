from django.db import models

# Create your models here.
class Hospital(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=100)
    x_ray = models.BooleanField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    pid = models.CharField(max_length=9)
    contacts = models.CharField(max_length=255)
    medical_history = models.TextField()
    status = models.BooleanField() #get cured or not

    def __str__(self):
        return self.name

class MedicalInstr(models.Model):
    name = models.CharField(max_length=100)
    intro = models.TextField()
    type = models.IntegerField()

    def __str__(self):
        return self.name



