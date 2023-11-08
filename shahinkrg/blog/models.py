from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    text = models.TextField(null=True)
    created = models.DateTimeField()
    def __str__(self):
        return self.title
