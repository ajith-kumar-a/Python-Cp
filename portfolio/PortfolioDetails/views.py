from django.shortcuts import redirect, render  
from PortfolioDetails.forms import UserImageForm  
from .models import UploadImage  
  
def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'PortfolioDetails/image_form.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm(request.POST, request.FILES)  
  
    return render(request, 'PortfolioDetails/image_form.html', {'form': form})
