from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('ShopName', 'ShopOwner')
        # fields = __all__
