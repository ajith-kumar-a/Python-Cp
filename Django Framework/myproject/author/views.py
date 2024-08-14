from django.shortcuts import render
from . models import author
from django.http import *

# Create your views here.

Author_name = author.objects.all()

auth_dict = {}
for auth in Author_name:
    auth_dict[auth.first_name] = auth


def index(request):
    auth_name = author.objects.all()
    return render(request,'author/index.html',
                  {
                      'author' : auth_name,

                  })


def Author_details_id(request,id):
    try:
        auth=author.objects.get(id=id)
       
        responce_data=render(request,'author/auth.html',{
            'text':auth
        })
        return HttpResponse(responce_data)
    except:
        raise Http404


def Author_details_slug(request,slug):
    try:
        auth=author.objects.get(slug=slug)
       
        responce_data=render(request,'author/auth.html',{
            'text':auth
        })
        return HttpResponse(responce_data)
    except:
        raise Http404

       
def Author_details(request,author):
   
    try:        
        author_detail = auth_dict[author]
       
        responce_data = render(request,'author/auth.html',{
            'text':author_detail,
        })
        return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound('This is not Mentioned')

