from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import Feedbackform
# Create your views here.
def feedbackform(request):
    if request.method == 'POST': #True
        # enter_username = request.POST['username']
        # print(enter_username)
        form = Feedbackform(request.POST)
 
        # if enter_username == "":
        #     return render(request,'userprofile/feedback.html',{
        #         'haserror':True
        #     })
        if form.is_valid():
            return HttpResponseRedirect('thankyou')
    form = Feedbackform()
 
    return render(request,'form_tab/feedback.html',{
        'form':form
    })
 
def thanku(request):
    return render(request,'form_tab/thank_you.html')