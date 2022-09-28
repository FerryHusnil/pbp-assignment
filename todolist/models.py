from django.db import models
import datetime
from django.contrib.auth import models as auth_models

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.now())
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
