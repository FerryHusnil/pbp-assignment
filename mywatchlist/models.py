from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.DateField()
    watched = models.BooleanField(default=False)
    review = models.TextField()