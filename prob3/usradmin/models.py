from django.db import models

# Create your models here.

class BasicUser(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254)
