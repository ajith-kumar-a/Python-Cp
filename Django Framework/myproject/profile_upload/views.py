from django.shortcuts import render
from .forms import Profileform
from django.views import View
from django.http import HttpResponseRedirect
from . models import ProfileImage

# Create your views here.

# def store_file(file):
#     with open('temp/image.jpg','+wb') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
 
# class CreateProfileView(View):
#     def get(self, request):
#         form = Profileform()
 
#         return render(request,'profileupload/userupload.html',{
#             'form':form
#         })
 
#     def post(self, request):
#         submittedform = Profileform(request.POST,request.FILES)
 
#         if submittedform.is_valid():
#             store_file(request.FILES['userimage'])
#             # profile = ProfileImage(userimage=request.FILES['userimage'])
#             # profile.save()
#             return HttpResponseRedirect('/profileupload/')
#         return render(request,'profileupload/userupload.html',{
#             'form':submittedform
#         })
 
from django.views.generic.edit import CreateView
from django.views.generic import ListView


class CreateProfileView(CreateView):
    model = ProfileImage
    template_name = "profileupload/userupload.html"
    success_url ='/profileupload'
    fields ="__all__"

class Profileview(ListView):
    model = ProfileImage
    template_name = 'profileupload/renderingImage.html' 
    context_object_name = 'renderingimg'
