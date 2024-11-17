from rest_framework import serializers
from BeerCollection.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'pk', "shop_name", "address",
        ]
