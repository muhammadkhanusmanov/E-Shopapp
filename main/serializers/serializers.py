from rest_framework.serializers import ModelSerializer
from ..models import Categories, Products, UsersProduct, MarketProduct, RecomntsProduct
from rest_framework import serializers

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ProductsSerialzer(ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = Products
        fields = '__all__'

class GoodsSerializer(ModelSerializer):
    product = ProductsSerialzer(many=True)
    class Meta:
        model = UsersProduct
        fields = '__all__'


class RProductsSerializer(ModelSerializer):
    '''get products in Mareting'''
    products = ProductsSerialzer(many=True)
    class Meta:
        model = MarketProduct
        fields = '__all__'


class RecomentSerializer(ModelSerializer):
    '''get recoment products'''
    products = ProductsSerialzer(many=True)
    class Meta:
        model = RecomntsProduct
        fields = '__all__'
