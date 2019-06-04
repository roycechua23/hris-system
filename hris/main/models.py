from django.db import models
from datetime import datetime 

# Create your models here.
class HR(models.Model):
    username = models.CharField(max_length=100)
    password = models.TextField()
    is_loggedin = models.BooleanField()
    date_lastlogin = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username