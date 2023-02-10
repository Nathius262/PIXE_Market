from rest_framework import serializers
from .models import Product, ProductTag

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
