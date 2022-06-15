from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    tel_type = models.CharField(max_length=100)
    number = models.IntegerField(null=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['firstname']