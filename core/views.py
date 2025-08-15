from django.shortcuts import render
from .forms import RatingForm
from .models import Resturant, Sale, Rating
from django.db.models import Sum, Prefetch
from django.utils import timezone
# Create your views here.


def index(request):
    #prefetch_related()
    # resturants = Resturant.objects.filter(name__istartswith = 'c').prefetch_related('ratings', 'sales')
    # context = {'resturants' : resturan''ts}
    #select_related() and only()
    #ratings = Rating.objects.all().only('rating', 'resturant__name').select_related('resturant') #foreign key resturant is passed
    #context = {'ratings' : ratings}
    # return render(request, 'index.html', context)       
    """
    Get all  5-star ratings, and fetch all the sales for resturants with 5-start ratings and sum the sales
    """
    #resturants =  Resturant.objects.prefetch_related('ratings', 'sales').filter(ratings__rating = 5).annotate(total = Sum('sales__income'))
    """
    Previously i got all the sales what if i want only the last month sales
    We will use Prefetch object NB: prefetch_related is different

    """
    month_ago = timezone.now() - timezone.timedelta(days=30)
    monthly_sales = Prefetch(
        'sales',
        queryset=Sale.objects.filter(datetime__gte = month_ago)
        
        )

    resturants =  Resturant.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating = 5)
    resturants = resturants.annotate(total  = Sum('sales__income'))
    print([r.total for r in resturants])
    return render(request, 'index.html')