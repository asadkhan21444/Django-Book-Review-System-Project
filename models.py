from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
 
   
class Book(models.Model):
    GENRE_CHOICES = [
        ('Mathematics', 'Mathematics'),
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('biology', 'Biology'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()  # This should exist
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    publication_date = models.DateField()
    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=0
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})