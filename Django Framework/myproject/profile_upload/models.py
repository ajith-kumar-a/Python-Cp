from django.db import models

# Create your models here.

class ProfileImage(models.Model):
    userimage = models.FileField(upload_to='image')