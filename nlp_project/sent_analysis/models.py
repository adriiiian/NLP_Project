from django.db import models

# Create your models here.
class SentAnalysis(models.Model):
    sentence = models.CharField(max_length=100)
