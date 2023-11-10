from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    portfolio = models.ImageField()

    def __str__(self):
        return self.title
