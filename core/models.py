from django.db import models

class Resturant(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    

    