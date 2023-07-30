from django.db import models
from django.forms import CharField

# Create your models here.
class GP(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100,null=True)
    number = models.IntegerField()

    def __str__(self):
        return self.name