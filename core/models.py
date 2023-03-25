from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    isOnline = models.BooleanField(default=True)
    isVerified = models.BooleanField(default=True)
    address1 = models.CharField(max_length=200, default='')
    address2 = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    zip = models.CharField(max_length=200, default='')
    website = models.CharField(max_length=250, default='')
    image_url = models.CharField(max_length=200, default='')
    
    
    def __str__(self):
        return self.name
