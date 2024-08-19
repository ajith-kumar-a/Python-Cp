from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator 
from django.utils.text import slugify

# Create your models here.

class portfolio_detail(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(18) , MaxValueValidator(50)])
    # city = models.CharField(max_length=100,null=True)
    # content = models.CharField(max_length=200,null=True)
    # read_more = models.CharField(max_length=300,null=True)
    # full_name = models.SlugField(default='',db_index=True,editable=False)


    # def save(self, *args, **kwargs):
    #     self.full_name = slugify(f'{self.first_name} {self.last_name}')
    #     super().save(*args,**kwargs)


    def __str__(self):
        return f'Author Details : -->   Full Name :  {self.first_name}  {self.last_name} ,  AGE : {self.age}  , City : {self.city} '
 
 