from django.db import models

from django.db import models

class AuthorizationUser(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    profession = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email_id = models.EmailField(unique=True)
    unique_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=256)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
