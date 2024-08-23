from django.shortcuts import render
from . models import portfolio_detail
from django.http import *

# Create your views here.


# def get_date(post):
#     return post['date']


def landing_page(request):
    portfolio = portfolio_detail.objects.all().order_by('-id')[:3]
    
    portfolio = portfolio[::-1]
  
    context = { 
        "data" : ['1', '2', '3'], 
        'users' : portfolio,
        
    } 
    return render(request, 'portfolio/landing_page.html', context)

def all_post(request):

    user = portfolio_detail.objects.all().order_by('first_name')
    context = { 
        "data" : [1, 2, 3,4,5,6,7,8], 
        'users' : user
    } 
    i=portfolio_detail.objects.get(id=9)

    print(i.img_title)

    return render(request,'portfolio/all_post.html',context)

def user_details_id(request,id):
    
    user=portfolio_detail.objects.get(id=id)
    context = { 
        'text':user
    } 
    
    return render(request,'portfolio/user_detail.html',context)

   
   