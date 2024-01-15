from django.db import models
from django.contrib.auth.models import User


class Cat(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    age = models.PositiveSmallIntegerField(null=False, blank=False)
    breed = models.CharField(max_length=100, null=False, blank=False)
    hairiness = models.CharField(max_length=100, null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cat"
        verbose_name_plural = "Cats"
