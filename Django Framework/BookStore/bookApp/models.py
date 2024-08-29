from django.db import models
from author.models import Author
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=60)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5),MinValueValidator(1)]
    )
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self) :
        return self.title 