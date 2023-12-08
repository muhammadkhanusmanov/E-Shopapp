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
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from .models import Categories,Products, UsersProduct,MarketProduct,RecomntsProduct

from .serializers.serializers import (
    CategorySerializer, ProductsSerialzer,GoodsSerializer, RProductsSerializer, RecomentSerializer
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

    def handle_exception(self, exc):
            if isinstance(exc, AuthenticationFailed):
                return Response({'detail': False, 'token': ''}, status=401)
            return super().handle_exception(exc)
    
class LogoutView(APIView):
    '''logout a user'''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delate(self,request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'status':'delated token'},status=status.HTTP_200_OK)
    

    
class CategoryView(APIView):
    '''get all categories'''
    def get(self,request):
        categories = Categories.objects.all()
        categories = CategorySerializer(categories,many=True).data
        return Response({'status':True,'categories':categories},status=status.HTTP_200_OK)

class ProductView(APIView):
    '''get all products'''
    def get(self,request):
        products = Products.objects.all()
        result = []
        for product in products:
            result.append(ProductsSerialzer(product).data)
        return Response({'status':True,'products':result},status=status.HTTP_200_OK)

    '''get products by category id'''
    def post(self, request,id:str):
        try:
            category = Categories.objects.get(id=id)
            products = Products.objects.filter(category=category)
            products = ProductsSerialzer(products,many=True).data
            category = CategorySerializer(category).data
            result = {'status':True,'category':category,'products':products}
            return Response(result,status=status.HTTP_200_OK)
        except:
            return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)
    
    '''get a product by id'''
    def put(self,request,id:str):
        try:
            product = Products.objects.get(id=id)
            product = ProductsSerialzer(product).data
            return Response({'status':True,'product':product},status=status.HTTP_200_OK)
        except:
            return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)


class SearchProduct(APIView):
    '''Search product'''
    def get(self,request,name:str):
        products = Products.objects.filter(name__icontains=name)
        products = ProductsSerialzer(products, many=True).data
        return Response({'status':True,'products':products},status=status.HTTP_200_OK)

import json

class BuyingView(APIView):
    '''a user orders products'''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        data = request.data
        data = dict(data)
        resp = {
            'product':data['products'],
            'user':user.id,
            'quanity':str(data['quanity']),
            'extra_number':data['extra_number'][0],
            'longitude':data['longitude'][0],
            'latitude':data['latitude'][0]
        }
        buying = GoodsSerializer(data=resp)
        if buying.is_valid():
            buying.save()
            return Response({'status': True},status=status.HTTP_201_CREATED)
        return Response({'status': False},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        user = request.user
        goods = UsersProduct.objects.filter(user=user)
        result = []
        data = GoodsSerializer(goods,many=True).data
        for i in data:
            result.append({"date":i["date"],"products":i["product"]})
        return Response({'status':True,'products':result},status=status.HTTP_200_OK)

class Reklama(APIView):
    '''get all marketing things'''
    def get(self, request):
        data = MarketProduct.objects.all()
        data = RProductsSerializer(data,many=True).data
        return Response({'status':True, 'data':data}, status=status.HTTP_200_OK)

class Recomentgoods(APIView):
    '''get all recoments products'''
    def get(self, request):
        data = RecomntsProduct.objects.all()
        data = RecomentSerializer(data,many=True).data
        return Response(data,status=status.HTTP_200_OK)
