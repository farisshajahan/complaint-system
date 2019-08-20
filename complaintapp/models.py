from django.db import models

# Create your models here.
class Complaint(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=20)
