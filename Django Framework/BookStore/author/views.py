from django.shortcuts import render
from . models import Author
from .serializers import AuthorSerializer
from rest_framework.viewsets import ModelViewSet
 
# Create your views here.
class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
 
    def list(self,request):
        try:
            author_objs = Author.objects.all()
            seri