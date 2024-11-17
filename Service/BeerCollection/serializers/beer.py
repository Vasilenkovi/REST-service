from rest_framework import serializers
from BeerCollection.models import Beer


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = [
            'pk', "name", "package", "type",
            "capacity", "price", "based",
            "flavorCommentary", "flavorCommentary",
            "mark", "shop"
        ]