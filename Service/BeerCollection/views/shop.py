from rest_framework import viewsets
from BeerCollection.models import Shop
from BeerCollection.serializers import ShopSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer