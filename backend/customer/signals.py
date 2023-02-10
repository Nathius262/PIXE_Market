from django.dispatch import receiver
from .models import Customer
from django.db.models.signals import post_save, post_delete
from PIL import Image

@receiver(post_delete, sender=Customer)
def submission_delete(sender, instance, **kwargs):
    instance.picture.delete(False)


@receiver(post_save, sender=Customer)
def save_img(sender, instance, *args, **kwargs):
    SIZE = 600, 600
    if instance.picture:
        pic = Image.open(instance.picture.path)
        try:
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(instance.picture.path)
        except:
            if pic.mode in ("RGBA", 'P'):
                pix = pic.convert("RGB")
                pix.thumbnail(SIZE, Image.LANCZOS)
                pix.save(instance.picture.path)