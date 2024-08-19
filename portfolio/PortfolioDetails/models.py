from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator 

# Create your models here.
class UploadImage(models.Model):  
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MaxValueValidator(50),MinValueValidator(18)],null= True)
    job_details = models.CharField(max_length=30)
    caption = models.CharField(max_length=400)  
    image = models.ImageField(upload_to='images')  
  
    def __str__(self):  
        return self.name,self.caption,self.age