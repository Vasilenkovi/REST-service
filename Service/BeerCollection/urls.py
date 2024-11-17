from django.urls import path, include
from rest_framework.routers import DefaultRouter
from BeerCollection.views import BeerViewSet, ShopViewSet


router = DefaultRouter()

router.register(r'beer', BeerViewSet, basename='beer')
router.register(r'shops', ShopViewSet, basename='shop')

urlpatterns = [
    path('', include(router.urls))
]
