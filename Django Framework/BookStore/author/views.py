from django.shortcuts import render
from . models import Author
from .serializers import AuthorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import status 

# # Create your views here.
# class AuthorViewset(ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
 
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return AuthorSerializer
#         return self.serializer_class
  
# #get all authors
#     def list(self,request):
#         try:
#             author_objs = Author.objects.all()
#             serializer = self.get_serializer(author_objs,many=True)
#             return Response({
#                 'status': status.HTTP_200_OK,
#                 'data':serializer.data
#             })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })
        
# # add an author
#     def create(self,request):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             if not serializer.is_valid():
#                 return Response({
#                     'status': status.HTTP_BAD_REQUEST,
#                     'data': serializer.errors,
#                     'message': 'Invalid data'
#                 })
#             serializer.save()

#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })

#     def retrive(self,request,pk=None):
#         try:
#             id = pk
#             if id is not None:
#                 author_objs = Author.objects.all()
#                 serializer = self.get_serializer(author_objs,many=True)
#                 return Response({
#                     'status': status.HTTP_200_OK,
#                     'data':serializer.data
#                 })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })


 
#     def destroy(self,request,pk):
#         try:
#             id=pk
#             author_objs = self.get_object()
#             author_objs.delete()
 
#             return Response({
#                 'status': status.HTTP_200_OK,
#                 'message':'Author deleted successfully'
#             })
 
#         except Exception as e:
#             print(e)
#             raise APIException({
#                 'message':APIException.default_detail,
#                 'status':APIException.status.code
#             })





# Create your views here.
class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
 
    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorSerializer
        elif self.action == 'create':
            return AuthorSerializer
        return self.serializer_class
 
#get all authors
    def list(self,request):
        try:
            author_objs = Author.objects.all()
            serializer = self.get_serializer(author_objs,many=True)
            return Response({
                'status': status.HTTP_200_OK,
                'data':serializer.data
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
#add an author
    def create(self,request):
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'Author Added Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
#get single author
 
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:
                author_objs = self.get_object()
                serializer = self.get_serializer(author_objs)
                return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
#update all fields of author
    def update(self,request):
        try:
            author_objs = self.get_object()
            serializer = self.get_serializer(author_objs,data=request.data,partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'Author Updated Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
 
 
#update specifie
    def partial_update(self,request):
        try:
            author_objs = self.get_object()
            serializer = self.get_serializer(author_objs,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':serializer.errors,
                    'message':'Inavlid Data'
                })
            serializer.save()
            return Response({
                    'status': status.HTTP_200_OK,
                    'data':serializer.data,
                    'message': 'Author Partial Updated Successfully'
                })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })
 
    def destroy(self,request,pk):
        try:
            id=pk
            author_objs = self.get_object()
            author_objs.delete()
 
            return Response({
                'status': status.HTTP_200_OK,
                'message':'Author deleted successfully'
            })
 
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status.code
            })