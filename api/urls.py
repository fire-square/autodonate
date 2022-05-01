"""URL patterns for API app."""

from typing import List

from django.urls import include, path
from django.urls.resolvers import URLPattern
from rest_framework import generics, mixins, routers, serializers, viewsets

from api.views import urls
from autodonate.models import Config, Donation, Player, Product


class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Config model."""

    class Meta:
        """Meta class."""

        model = Config
        fields = ["key", "value", "read_only"]


class ConfigViewSet(viewsets.ModelViewSet):
    """Config viewset model."""

    queryset = Config.objects.filter(public=True)
    serializer_class = ConfigSerializer


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Product model."""

    class Meta:
        """Meta class."""

        model = Product
        fields = ["id", "name", "price", "long_description", "group", "max_in_cart", "image"]


class ProductViewSet(viewsets.ModelViewSet):
    """Product viewset model."""

    queryset = Product.objects.filter(enabled=True)
    serializer_class = ProductSerializer


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Player model."""

    class Meta:
        """Meta class."""

        model = Player
        fields = ["nickname"]


class PlayerViewSet(generics.RetrieveAPIView, viewsets.GenericViewSet):
    """Viewset for Player model."""

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class DonationSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Donation model."""

    product = ProductSerializer(read_only=True)
    player = PlayerSerializer(read_only=True)

    class Meta:
        """Meta class."""

        model = Donation
        fields = ["id", "product", "player", "date"]


class DonationViewSet(viewsets.ModelViewSet):
    """Serializer for Donation model."""

    queryset = Donation.objects.filter(product__enabled=True)[:6]
    serializer_class = DonationSerializer


router = routers.DefaultRouter()
router.register(r"config", ConfigViewSet)
router.register(r"product", ProductViewSet)
router.register(r"player", PlayerViewSet)
router.register(r"donation", DonationViewSet)

urlpatterns: List[URLPattern] = [
    path("", include(router.urls)),
]

urlpatterns.extend(urls)
