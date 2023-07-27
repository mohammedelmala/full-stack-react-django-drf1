from django.conf import settings
from django.db import models

from . import serializers
from .validators import validate_icon_image_size, validate_image_file_extension


def category_icon_upload_path(instance, filename):
    return f'category/{instance.id}/category_icon/{filename}'

def server_icon_upload_path(instance, filename):
    return f'server/{instance.id}/server_icon/{filename}'

def server_banner_upload_path(instance, filename):
    return f'server/{instance.id}/server_banner/{filename}'

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to=category_icon_upload_path, null=True, blank=True, validators=[validate_icon_image_size, validate_image_file_extension])
    
    # def save(self, *args, **kwargs):
    #     if self.id:
    #         this = get_object_or_404(Category,id=self.id)

    #     super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name  


class Server(models.Model):
    name= models.CharField(max_length=100)
    owner= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='server_owner')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='server_category')
    description = models.TextField(max_length=250, null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name
    


class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='channel_owner')
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="channel_server")
    banner = models.ImageField(upload_to=server_banner_upload_path, blank=True, null=True, validators=[validate_image_file_extension])
    icon = models.ImageField(upload_to=server_icon_upload_path, blank=True, null=True, validators=[validate_icon_image_size,validate_image_file_extension])

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel,self).save(*args,**kwargs)
    

    def __str__(self):
        return self.name
    



