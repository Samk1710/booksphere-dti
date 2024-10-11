# library_app/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='covers/')
    pdf_file = models.FileField(upload_to='pdfs/')
    
    def __str__(self):
        return self.title