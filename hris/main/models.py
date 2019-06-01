from django.db import models

# Create your models here.
class HR(models.Model):
    username = models.CharField(max_length=100)
    password = models.TextField()

    def __str__(self):
        return self.username