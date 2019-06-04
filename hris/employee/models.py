from django.db import models
from datetime import datetime

# Create your models here.
class Employee(models.Model):

    username = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True, upload_to="employee_images")
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    date_hired = models.DateField()
    tin = models.CharField(max_length=30)
    philhealth = models.CharField(max_length=30)
    sss = models.CharField(max_length=30)
    pag_ibig = models.CharField(max_length=30)
    date_updated = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.name