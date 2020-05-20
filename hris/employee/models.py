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
    department = models.CharField(max_length=100, blank=True)
    supervisor = models.CharField(max_length=100, blank=True)
    salary = models.PositiveIntegerField(default=0)
    date_hired = models.DateField()
    tin = models.CharField(max_length=30, blank=True)
    philhealth = models.CharField(max_length=30, blank=True)
    sss = models.CharField(max_length=30, blank=True)
    pag_ibig = models.CharField(max_length=30, blank=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.first_name} {self.middle_name} {self.last_name}"