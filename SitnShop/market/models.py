from django.db import models
from django.conf import settings


class Shop(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ShopOwner = models.CharField(max_length=255)
    ShopName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    NumOfAds = models.IntegerField()
    Advertisement = models.FileField()
    ProfilePic = models.FileField()

    timestamp = models.DateTimeField()


    def __str__(self):
        return str(self.ShopName)

class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followingShops = models.ManyToManyField(Shop, related_name='interested_shops', blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return str(self.user.username)
