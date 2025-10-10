from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField()
    surname = models.CharField()
    feedback = models.TextField()
    rating = models.PositiveIntegerField()