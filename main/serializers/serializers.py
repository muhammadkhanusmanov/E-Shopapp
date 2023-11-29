from rest_framework.serializers import ModelSerializer
from ..models import Categories, Products
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