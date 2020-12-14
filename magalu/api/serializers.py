from rest_framework import serializers
from api.models import Client, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    favorite = ProductSerializer(read_only=True, many=True)
    favorite_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='favorite',
        many=True
    )
    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'favorite', 'favorite_id')



        