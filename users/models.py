from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    passport_no = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    role = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.user.username} profile'
