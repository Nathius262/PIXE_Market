from django.shortcuts import render
from rest_framework.viewsets import generics, mixins
from .serializers import ProductSerializers
from .models import Product
from rest_framework.response import Response

# Create your views here.

class ProductViewSet(generics.ListAPIView, mixins.ListModelMixin):
    serializer_class =ProductSerializers
    queryset = Product.objects.all()
    
    def get(self, request):
        return self.list(request)
