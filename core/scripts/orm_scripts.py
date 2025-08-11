from core.models import Resturant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

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


# def run():
#     Sale.objects.create(
#         resturant =  Resturant.objects.first(),
#         income = 12.33,
#         datetime = timezone.now()
#     )
#     Sale.objects.create(
#         resturant =  Resturant.objects.first(),
#         income = 92.33,
#         datetime = timezone.now()

#     )
#     Sale.objects.create(
#         resturant =  Resturant.objects.first(),
#         income = 27.33,
#         datetime = timezone.now()

#     )




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
filter,exclude Lookup:  __gte ,__lte, 
"""

# def run():
#     # print(Rating.objects.filter(rating = 3)) #rating is a field must be exactly same name as field (Fieldname = value)
#     # print(Rating.objects.filter(rating__gte = 3)) #lookup WHERE
#     # print(Rating.objects.filter(rating__lte = 5)) #lookup WHERE
#     print(Rating.objects.exclude(rating__lte = 5)) #lookup WHERE NOT
#     # print(Rating.objects.filter(rating = 5))
#     # print(Rating.objects.filter(rating = 7))
#     print(connection.queries)

"""
Updating Records

"""


# def run():
#     resturant  =   Resturant.objects.first()
#     print(resturant.name)
#     resturant.name = "Olee"
#     resturant.save()
#     print(resturant.name)
#     pprint(connection.queries)


"""SQL TOPIC: JOIN
Querying related records
"""

# def run():
#     rating  = Rating.objects.first()
#     print(rating.rating)
#     print(rating.resturant)
#     print(rating.resturant.name)
#     print(rating.resturant.latitude)
#     pprint(connection.queries)


"""
Reverse Relation: 
Context: 
        Suppose in the Resturant there is no rating field but Rating model has
        resturant field foreign key. So how can i get the rating by using Resturant
        model which doesn't have any rating field???

Answer:  Reverse Relation
"""


# def run():
#     # resturant = Resturant.objects.first()
#     # print(resturant.ratings.all()) #set a related name of ratings | or without related names, rating_set
#     # pprint(connection.queries)
#     resturant = Resturant.objects.first()
#     print(resturant.sales.first().income)
    


"""
Get or Create METHOD
"""


# def run():
#     user = User.objects.first()
#     resturant = Resturant.objects.first()
#     rating,created =  Rating.objects.get_or_create(
#             resturant = resturant,
#             user = user,
#             rating = 2,)

#     pprint(f'Rating: {rating} Created : {created}' )

"""
Using Django validators, Automatically doesn't WORK but if you call
full_clean() then it throws an exception 
"""

# def run():
#     user = User.objects.first()
#     resturant = Resturant.objects.first()
#     rating = Rating(
#         user = user,
#         resturant = resturant,
#         rating = 9
#     )
#     rating.full_clean()
#     rating.save()


"""
Update: Specifying which exact field to update beforehand

"""


# def run(): 
#     resturant = Resturant.objects.first()
#     print(resturant.name)
#     resturant.name = 'New Resturant name'
#     resturant.save(
#         update_fields=['name'] #using this only updates this field other things untouched
#     )
#     pprint(connection.queries)


"""
Updating a queryset of records with
queryset update() method

"""

# def run(): 
#     resturant = Resturant.objects.all()
#     resturant.update(
#         date_opened = timezone.now()
#     )
#     print(connection.queries)

"""
Filtering queryset with a startswith lookup
django and updating multiple arguments

"""

# def run(): 
#     resturant = Resturant.objects.filter(name__startswith= 'P')
#     print(resturant.update(
#         date_opened = timezone.now() - timezone.timedelta(days=365), 
#         website = "https://test.me"
#     ))
#     print(connection.queries)


"""
Delete

"""

def run(): 
    resturant = Resturant.objects.first()
    print(resturant.pk)
    print(resturant.ratings.all())
    print(connection.queries)