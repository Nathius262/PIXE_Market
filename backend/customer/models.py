from django.db import models
from backend.user.models import CustomUser
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
import os
from django.conf import settings


def upload_location(instance, filename):
    file_path = 'profile/user_{user_id}/{name}_profile.jpeg'.format(
        user_id=str(instance.user.id), name=str(instance.user.email), filename=filename
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=False)
    first_name = models.CharField(max_length=100, verbose_name="first_name", blank=True, null=True)
    last_name = models.CharField(max_length=100, verbose_name="last_name", blank=True, null=True)
    picture = models.ImageField(upload_to=upload_location, null=True, blank=True, default="user.png")

    def __str__(self):
        return str(self.user)

    @property
    def picture_url(self):
        try:
            picture = self.picture.url
        except :
            picture =""
        return picture


class SellerTags(MPTTModel):
    tag = models.CharField(max_length=50, null=True, blank=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="tag_parent")
    date_updated = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = "Seller Tags"

    class MPTTMeta:        
        order_insertion_by = ['date_updated']
        

    def __str__(self):
        full_path = [self.tag]
        p = self.parent
        while p is not None:
            full_path.append(p.tag)
            p = p.parent
        return ' -> '.join(full_path[::-1])

class Seller(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=False)
    tag = models.ManyToManyField(SellerTags, blank=True, related_name="seller_tag")
    discription = models.TextField(help_text="Short discription of your products")
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or str(self.user)

