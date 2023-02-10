from django.urls import path
from .views import SellerViewSet, CustomerViewSet

app_name = 'customer'

urlpatterns = [
    path('seller/', SellerViewSet.as_view()),
    path('customer/', CustomerViewSet.as_view()),
    ]