from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
USER = get_user_model()
class Blog (models.Model):
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField(default=None)
    images = models.ImageField(default=None)
    content = models.TextField()

    def __str__(self):
        return self.title