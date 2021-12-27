from django.db import models, reset_queries

# Create your models here.

class Person(models.Model):
    email = models.EmailField(verbose_name='email',max_length=60, unique=True)
    name = models.CharField(verbose_name='name', max_length=30)
    age = models.IntegerField(verbose_name='age')

    def __str__(self):
        return self.email


