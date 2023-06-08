from django.db import models

# Create your models here.

class Item(models.Model):
    num=models.IntegerField()
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.name
