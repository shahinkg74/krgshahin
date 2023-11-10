from django.shortcuts import render
from .models import Portfolio


# Create your views here.

def portfolio(request):
    all = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'all': all})
