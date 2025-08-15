from django.shortcuts import render
from .forms import RatingForm
from .models import Resturant, Sale, Rating
# Create your views here.


def index(request):
    resturants = Resturant.objects.all().prefetch_related('ratings')
    context = {'resturants' : resturants}
    return render(request, 'index.html', context)       