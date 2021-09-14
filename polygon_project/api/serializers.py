from .models import *
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class PolygonAreaSerializer(serializers.ModelSerializer):
    provider = serializers.CharField(source='provider_name.name')
    class Meta:
        model = PolygonArea
        fields = ['name', 'price', 'geojson', 'provider']