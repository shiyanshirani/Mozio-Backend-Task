from .models import *
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class PolygonAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolygonArea
        fields = "__all__"
