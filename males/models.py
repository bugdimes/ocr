from django.db import models

# Create your models here.

class Male(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)