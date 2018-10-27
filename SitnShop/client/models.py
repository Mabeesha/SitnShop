from django.db import models
from django.conf import settings
from django.core.validators import int_list_validator

# Create your models here.


class Client(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    NumofAds = models.IntegerField()
    Advertisement = models.FileField()
    ProfilePic = models.FileField()

    timestamp = models.DateTimeField()


    def __str__(self):
        return str(self.Name)
