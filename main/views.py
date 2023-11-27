from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpRequest,JsonResponse,FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from .models import Category

from .serializers.serializers import (
    CategorySerializer
)



class RegisterView(APIView):
    '''Sign up a user'''
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        number = data.get('number')
        try:
            user = User.objects.get(first_name=number)
            return Response({'status':'This number is already'},status=status.HTTP_208_ALREADY_REPORTED)
        except:
            try:
                user = User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = number
                )
                token = Token.objects.create(user=user)
                return Response({'status':'Create a user', 'token':token.key},status=status.HTTP_201_CREATED)
            except:
                return Response({'status':'This username is already'},status=status.HTTP_208_ALREADY_REPORTED)
    
class UserView(APIView):
    authentication_classes = [BasicAuthentication]
    '''login user'''
    def post(self, request):
        user = request.user
        token = Token.objects.get_or_create(user=user)
        token = str(token[0])
        return Response({'detail':True,'token':token},status=status.HTTP_201_CREATED)
    
class LogoutView(APIView):
    '''logout a user'''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delate(self,request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'status':'delated token'},status=status.HTTP_200_OK)
    
class CategoryImg(APIView):
    def get(self, request,id:str):
        try:
            category = Category.objects.get(id=id)
            img =category.photo 
            file = open(img.path, 'rb')
            resp = FileResponse(file)
            return resp
        except:
            return Response({'status':False}, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryView(APIView):
    '''get all categories'''
    def get(self,request):
        categories = Category.objects.all()
        resuts = []
        for category in categories:
            a = CategorySerializer(category).data
            a['photo']=f'http://ebozorapi.pythonanywhere.com/api/v2/save/{a["id"]}'
            resuts.append(a)
        return Response({'status':True,'categories':resuts},status=status.HTTP_200_OK)




