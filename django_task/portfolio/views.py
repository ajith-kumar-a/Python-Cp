from django.shortcuts import render
from . models import portfolio_detail,Comment
from django.http import *
   
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Comment

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.


# def get_date(post):
#     return post['date']


def landing_page(request):
    portfolio = portfolio_detail.objects.all().order_by('-id')[:3]
    
    portfolio = portfolio[::-1]
  
    context = { 
        # "data" : ['1', '2', '3'], 
        'users' : portfolio,
        
    } 
    return render(request, 'portfolio/landing_page.html', context)


def all_post(request):

    user = portfolio_detail.objects.all().order_by('first_name')
    context = { 
        # "data" : [1, 2, 3,4,5,6,7,8], 
        'users' : user
    } 
    return render(request,'portfolio/all_post.html',context)



def user_details_id(request,id):
    
    user=portfolio_detail.objects.get(id=id)
    comment = Comment.objects.all()
    context = { 
        'text':user,
        'comments': comment
    } 
    
    return render(request,'portfolio/user_detail.html',context)

def user_details_slug(request, slugs):
    # Fetch the portfolio_detail object, or return a 404 if not found
    user = get_object_or_404(portfolio_detail, full_name=slugs)
    
    # Fetch comments related to the specific portfolio_detail object
    comments = Comment.objects.filter(post=user)
    
    context = { 
        'text': user,
        'comments': comments
    } 
    
    return render(request, 'portfolio/user_detail.html', context)

class AddPost(CreateView):
    model = portfolio_detail
    template_name = "portfolio/add_post.html"
    success_url = reverse_lazy('all-post')  # Redirect after successful submission

    # Explicitly define the fields to be used in the form
    fields = ['first_name', 'last_name', 'age','city','content','read_more','event_date','event_time','img_url','img_title','author','tags']  # List fields as needed

class AddComment(CreateView):
    model = Comment
    template_name = "portfolio/add_comment.html"
    success_url = reverse_lazy('all-post')  # Redirect after successful submission

    # Explicitly define the fields to be used in the form
    fields = ['user_name', 'user_email', 'comment']  # List fields as needed

    def get_initial(self):
        initial = super().get_initial()
        post_id = self.request.GET.get('post_id')
        if post_id:
            post = get_object_or_404(portfolio_detail, id=post_id)
            initial['post'] = post
        return initial

    def form_valid(self, form):
        post_id = self.request.GET.get('post_id')
        if post_id:
            form.instance.post = get_object_or_404(portfolio_detail, id=post_id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.request.GET.get('post_id')
        if post_id:
            context['post'] = get_object_or_404(portfolio_detail, id=post_id)
        return context
# class Profileview(ListView):
#     model = Comment
#     template_name = 'portfolio/renderingImage.html' 
#     context_object_name = 'renderingimg'
