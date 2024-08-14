from django.shortcuts import render
from . models import author
from django.http import *

# Create your views here.

Author_name = author.objects.all()

auth_dict = {}
for auth in Author_name:
    auth_dict[auth.first_name] = auth


def index(request):
    auth_name = list(auth_dict.keys())
    return render(request,'author/index.html',
                  {
                      'author' : auth_name,

                  })


def Author_details_id(request,author_id):
    try:
        


def Author_details(request,author):
   
    try:        
        author_detail = auth_dict[author]
       
        responce_data = render(request,'author/auth.html',{
            'text':author_detail,
        })
        return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound('This is not Mentioned')

