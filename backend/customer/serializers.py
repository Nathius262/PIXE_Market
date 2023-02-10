from rest_framework import serializers
from .models import Seller, Customer
from backend.user.models import CustomUser
from rest_framework import validators

class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField
    class Meta:
        model = Customer
        exclude = ['id',]

    def get_user (self, obj):
        return self.obj.user



class SellerSerializer(serializers.ModelSerializer):

    user=serializers.SerializerMethodField()
    tag=serializers.SerializerMethodField()

    class Meta:
        model = Seller
        exclude = ['id',]

    def get_user(self, obj):
        return obj.user.email

    def get_tag(self, obj):
        try:
            tag_list = []
            for items in obj.tag.all():
                tag_list.append(items.tag)
            return tag_list
        except TypeError:
            return obj.tag
        except AttributeError:
            return None