from django.db import models

# Create your models here.


class sourceTable(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_accessed = models.DateField()
    date_added = models.DateTimeField()
