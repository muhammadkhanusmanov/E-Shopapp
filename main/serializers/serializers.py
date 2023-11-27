from rest_framework.serializers import ModelSerializer
from ..models import Categories, Products

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ProductsSerialzer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Products
        fields = '__all__'