from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Book(models.Model):

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:index')
    
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    status = models.CharField(max_length=30)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], db_index=True)
    image = models.URLField(max_length=10000, default='https://harpercollins.co.in/wp-content/uploads/placeholder/book-placeholder.jpg')

