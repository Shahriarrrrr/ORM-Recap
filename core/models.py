from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.functions import Lower



class Resturant(models.Model):

    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        BANGLADESHI = 'BN', 'Bangladeshi'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        FASTFOOD = 'FF', 'Fast Food'
        MEXICAN = 'MX', 'Mexican'
        OTHER = 'OT', 'Other'


    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    resturant_type = models.CharField(max_length=2, choices=TypeChoices.choices, default='' )



    #Setting default ordering
    class Meta:
        ordering = [Lower('name'), 'date_opened']   #if name same then date_opened
        get_latest_by = 'date_opened'


    def __str__(self):
        return self.name
    
    #Checking what we are doing
    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE , related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"Rating : {self.rating}"
    

class Sale(models.Model):
    resturant = models.ForeignKey(Resturant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField() 


class Staff(models.Model):
    name = models.CharField(max_length=255)
    resturants = models.ManyToManyField(Resturant, related_name='staff', through='StaffResturant')

class StaffResturant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    resturant = models.ForeignKey(Resturant, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)