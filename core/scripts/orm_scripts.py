from core.models import Resturant, Rating, Sale, Staff
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

# def run(): 
#     resturant = Resturant.objects.first()
#     print(resturant.pk)
#     print(resturant.ratings.all())
#     resturant.delete()
#     print(connection.queries)


"""
Delete  ALL

"""

# def run(): 
#     Resturant.objects.all().delete()
#     print(connection.queries)



"""
Initial Count

"""


# def run():
#     print(Resturant.objects.count())
#     print(Rating.objects.count())
#     print(Sale.objects.count())



"""
Filtering RECORDS Single

"""

# def run():
#     #filter down only to chinese resturants
#     chinese_resturants =  Resturant.objects.filter(resturant_type = Resturant.TypeChoices.CHINESE)
#     #print(chinese_resturants)

#     #Filter by name
#     #print(Resturant.objects.filter(name = 'Pizzeria 1'))


#     """
#     get() method can only work if there is a single row
#     and returns model instance , multiples will not work
#     """

#     #print(Resturant.objects.get(name = 'Pizzeria 1')) #This will work
#     #print(Resturant.objects.get(resturant_type = Resturant.TypeChoices.ITALIAN)) #This will not work because there is > 5 italian

#     italian = Resturant.objects.filter(resturant_type = Resturant.TypeChoices.ITALIAN)
#     #print(italian)
#     print(italian.exists()) #Returns Boolean
#     #pprint(connection.queries)


"""
Filter Multiple AND conditions

startswith, __in, exclude()

"""    


# def run():
#     chinese = Resturant.TypeChoices.CHINESE
#     mexican = Resturant.TypeChoices.MEXICAN
#     indian = Resturant.TypeChoices.INDIAN

#     check_types = [chinese, mexican, indian]
    
#     #resturants =  Resturant.objects.filter(resturant_type = chinese , name__startswith = 'C')
#     #resturants =  Resturant.objects.filter(resturant_type__in = check_types)
#     #resturants =  Resturant.objects.exclude(resturant_type = chinese)
#     resturants =  Resturant.objects.exclude(resturant_type__in = [chinese, indian])
#     print(resturants)
#     pprint(connection.queries)


"""
Suppose we want the resturants which name starts with a,b,c,d
lt, gt
"""

# def run():
#     #resturants = Resturant.objects.filter(name__lt = 'E') #Suppose we want the resturants which name starts with a,b,c,d
#     #resturants = Resturant.objects.filter(longitude__gt = 0) #Suppose we want the resturants which name starts with a,b,c,d
#     sales =  Sale.objects.filter(income__gt = 90)
#     print(sales)
#     #print(resturants)
#     pprint(connection.queries)



"""
range lookups can be alsp used on datetime

"""

# def run():
#     sales = Sale.objects.filter(income__range = (50, 60))
#     print([sale.income for sale in sales])
#     pprint(connection.queries)





"""
ORDER BY

order_by(), order_by().reverse
"""
from django.db.models.functions import Lower

# def run():
#     #resturants = Resturant.objects.order_by('name') #Ascending name alphabetical
#     #resturants = Resturant.objects.order_by('-name') #Reverse order can be used with number, datetimefield etc
#     #resturants = Resturant.objects.order_by('name').reverse()
#     """
#     Suppose there is a lower case name then it wont take account of that . How to tackel this?
#     """
#     #resturants = Resturant.objects.order_by(Lower('name')) #To avoid cases
#     #print(resturants)

#     """
#     Order by date opened
#     """
#     #resturants = Resturant.objects.order_by('date_opened')[2:5]

#     """
#     Model edited to lower behaviour
#     """
# #     resturants = Resturant.objects.all()
# #     print(resturants)
# #     pprint(connection.queries)

"""
earliest()
latest()

Used for date time

"""


# def run():
#         #resturant =  Resturant.objects.earliest('date_opened')
#         #resturant =  Resturant.objects.latest('date_opened')
#         resturant =  Resturant.objects.latest() #pre defined in model
#         print(resturant)
#         pprint(connection.queries)


"""
filtering by foreign keys

"""


# def run():
#         chinese = Resturant.TypeChoices.CHINESE
#         sales = Sale.objects.filter(resturant__resturant_type = chinese)
#         print(sales)
#         pprint(connection.queries)



"""
Prefetch()
select_related()

See in views
"""

"""
Many to Many fields and Through models 
for many to many relationship

"""
"""
Created a staff 
then printed if the staff is working in a resturant
then added a resturant 
Printed again....etc
add, all, remove, count, set,clear
"""

# def run():
#     staff, created = Staff.objects.get_or_create(name = 'John Wick')
# #     print(staff.resturants.all())


# #     staff.resturants.add(Resturant.objects.first())
# #     staff.resturants.remove(Resturant.objects.first())
#     #staff.resturants.set(Resturant.objects.all()[:5])
#     staff.resturants.clear()
#     print(staff.resturants.all())
#     print(staff.resturants.count())

"""
Now for the other side of Many to Many

"""

def run():

    resturant = Resturant.objects.get(pk = 20)

    staff =  resturant.staff.all()
    print(staff)