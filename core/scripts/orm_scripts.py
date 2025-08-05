from core.models import Resturant, Rating
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User

#SEEDING DATA
# def run():
#     resturant = Resturant()
#     resturant.name = "My Italian Resturant"
#     resturant.latitude = 50.2 
#     resturant.longitude = 50.2
#     resturant.date_opened = timezone.now()
#     resturant.resturant_type = Resturant.TypeChoices.ITALIAN
#     resturant.save()

#QUERYING
# def run():
#     # resturant = Resturant.objects.all() # returns all
#     # resturant = Resturant.objects.first() # returns first row
#     resturant = Resturant.objects.all()[0] # returns first instance
#     print(resturant)
#     print(connection.queries)


#Another way to create a record without .save()
# def run():
#     Resturant.objects.create(
#         name = "Pizza Shop",
#         date_opened = timezone.now(),
#         resturant_type = Resturant.TypeChoices.ITALIAN,
#         latitude = 50.2,
#         longitude = 50.2,
#     )
#     print(connection.queries)


"""
count, last, 

"""
# def run():
#     print(Resturant.objects.count())
#     print(Resturant.objects.last())
#     print(connection.queries)



#Storing rating with  foreign keys

# def run():
#     resturant =  Resturant.objects.first()
#     user = User.objects.first()
#     Rating.objects.create(
#         user = user,
#         resturant = resturant,
#         rating = 3
#     )


"""

"""

def run():
    print(Rating.objects.all())


