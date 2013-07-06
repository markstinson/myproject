from django.db import models

# Create your models here.

class Contact(models.Model):
    """docstring for Contact model """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    website_url = models.URLField(blank=True)