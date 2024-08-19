from django.shortcuts import render
from . models import portfolio_detail
from django.http import *

# Create your views here.


def get_date(post):
    return post['date']
 
# # Create your views here.
# def starting_page(request):
#     sorted_posts=sorted(all_posts,key=get_date)
#     latest_posts = sorted_posts[-3:]
#     return render(request,"Blog/index.html",{
#         "posts":latest_posts
#     }
#     )

def landing_page(request):
    portfolio = portfolio_detail.objects.all()
    print(portfolio)
    user1=portfolio_detail.objects.get(id=1)
    user2=portfolio_detail.objects.get(id=2)
    user3=portfolio_detail.objects.get(id=3)



    context = { 
        "data" : ['1', '2', '3'], 
      
        'user1' : user1,
        'user2' : user2,
        'user3' : user3,
    } 
    return render(request,'portfolio/landing_page.html',context)

def all_post(request):

    user = portfolio_detail.objects.all().order_by('first_name')
    context = { 
        "data" : [1, 2, 3,4,5,6,7,8], 
        'users' : user
    } 

    return render(request,'portfolio/all_post.html',context)

def user_details_id(request,id):
    
    user=portfolio_detail.objects.get(id=id)
    context = { 
        'text':user
    } 
    
    return render(request,'portfolio/user_detail.html',context)

   
   