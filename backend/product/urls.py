from django.urls import path
from .views import ProductViewSet

app_name = 'product'

urlpatterns = [
    path('', ProductViewSet.as_view()),
    ]