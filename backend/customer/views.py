from rest_framework.viewsets import generics, mixins
from rest_framework.response import Response
from .models import Customer, Seller
from backend.user.models import CustomUser
from .serializers import SellerSerializer, CustomerSerializer

class CustomerViewSet(generics.ListAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        user = request.data['user']
        user_obj = CustomUser.objects.all()
        new_user = ""
        if user_obj.filter(email=user):
            new_user = user_obj.filter(email=user)
        elif user_obj.filter(phone=user):
            new_user = user_obj.filter(phone=user)
        else:
            return Response({"user": "user with this name does not exist please signup"})
        customer = self.create(request)
        print(customer)
        return customer

class SellerViewSet(generics.ListAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    
    def get(self, request):
        return self.list(request)

    def post(self, request):        
        return self.create(request)