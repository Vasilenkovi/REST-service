from rest_framework import viewsets
from BeerCollection.models import Beer
from BeerCollection.serializers import BeerSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

