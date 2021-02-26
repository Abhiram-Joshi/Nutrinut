from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    birthdate = models.DateField(blank=True)
    weight = models.PositiveIntegerField(blank=True)
    height = models.PositiveIntegerField(blank=True)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class FoodCalories(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return self.name
