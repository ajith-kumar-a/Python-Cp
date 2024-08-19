from django.shortcuts import render
from . models import portfolio_detail

# Create your views here.


def lanfing_page(request):
    portfolio = portfolio_detail.objects.all()
    print(portfolio)
    return render(request,'details/landing_page.html')