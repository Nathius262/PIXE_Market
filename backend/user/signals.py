from backend.customer.models import Customer
from .models import CustomUser
from django.db.models.signals import post_save


def create_customer(sender, instance, *args, **kwargs):
    customer = Customer.objects.all().get_or_create(user=instance)
    return customer

post_save.connect(create_customer, sender=CustomUser)