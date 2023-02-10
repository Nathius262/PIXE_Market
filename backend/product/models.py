from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from autoslug import AutoSlugField
from django.conf import settings
from backend.customer.models import Seller
from mptt.models import MPTTModel, TreeForeignKey


def product_image_location(instance, filename):
	file_path = 'product/{product_id}/{product_name}.jpeg'.format(
		product_id=instance.product_owner, product_name =instance.product_name, filename=filename
	)
	full_path = os.path.join(settings.MEDIA_ROOT, file_path)
	if os.path.exists(full_path):
		os.remove(full_path)
	return file_path

class ProductTag(MPTTModel):
    tag_name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="product_parent")
    date_updated = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.tag_name


class Product(models.Model):
    product_owner = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=False)
    product_name = models.CharField(max_length=200, null=True)
    product_description = models.TextField(blank=True)
    category = models.ForeignKey(ProductTag, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    slug = AutoSlugField(populate_from="product_name", unique=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    product_image = models.ImageField(upload_to=product_image_location, null=True, blank=True)

    @property
    def product_image_url(self):
        try:
            url = self.product_image.url
        except:
            url = ""

        return url

    def __str__(self):
        return self.product_name


@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.product_image.delete(False)
