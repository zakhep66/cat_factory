from django.db import models
from django.contrib.auth.models import User


class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    breed = models.CharField(max_length=100)
    hairiness = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cat"
        verbose_name_plural = "Cats"
