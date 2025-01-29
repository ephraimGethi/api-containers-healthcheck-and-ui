from django.db import models
from django.conf import settings
# Create your models here.

class computer(models.Model):
    name = models.TextField()
    avatar = models.FileField(upload_to='avatar',null=True,blank=True)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def image_url(self):
        return f"{settings.SITE_URL}{self.avatar.url}"
    
class Rooms(models.Model):
    name = models.TextField()
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
