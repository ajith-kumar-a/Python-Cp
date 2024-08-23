# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .form import Feedbackform
# from .models import Review
# # Create your views here.
# def feedbackform(request):
#     if request.method == 'POST': #True
#         # enter_username = request.POST['username']
#         # print(enter_username)
#         print("hi")
#         form = Feedbackform(request.POST)
 
#         # if enter_username == "":
#         #     return render(request,'userprofile/feedback.html',{
#         #         'haserror':True
#         #     })
#         print("hiii")

#         if form.is_valid():

#             review = Review(
#                 user_name = form.cleaned_data['user_name'],
#                 text = form.cleaned_data['text'],
#                 rating = form.cleaned_data['rating']
#             )
#             review.save()
#             print(form.cleaned_data)
#             return HttpResponseRedirect('thankyou')
#         print("hittii")

#     else :
#         form = Feedbackform()

 
#     return render(request,'form_tab/feedback.html',{
#         'form':form
#     })
 
# def thanku(request):
#     return render(request,'form_tab/thank_you.html')


from django.shortcuts import render
from django.http import *
from .form import Feedbackform
from .models import *
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views import View

# Create your views here.

class FormsViews(View):

    def get(self,request):
        form = Feedbackform()
        return render(request, "form_tab/feedback.html", {"form":form})

    def post(self,request):
        form = Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thankyou")
        return render(request,"form_tab/feedback.html", {"form":form })
        
    # 
        # if request.method == "POST":
        #     form_data = details(request.POST) # i will get the data from the froms
        #     if form_data.is_valid(): # i it check it is valid are nt inside the html page it self 
        #         # datas = Review(
        #         #     user_name = form_data.cleaned_data["user_name_2"],
        #         #     review = form_data.cleaned_data["rating"],
        #         #     message = form_data.cleaned_data["message"]
        #         # )
        #         form_data.save()
        #         return HttpResponseRedirect("feedback")
        # else:
        #     form_data = details() # it will act like the form and we written in the forms.py 
        # return render(request,"forms/forms.html", {"form":form_data})

class Template(TemplateView):
    template_name = "form_tab/thankyou.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Messgae"] = "somthing Here" 
        context["hello"] = "hello" 
        context["threee"] = "hi" 
        return context

class feedbacklistView(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "form_tab/feedlist.html"