from rest_framework import serializers
from .models import Location, LocationDetail


class LocationSerializer(serializers.Serializer):
    class Meta:
        model = Location
        fields = ['id', 'img', 'city', 'topic', 'title', 'reading_is']


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDetail
        fields = ['title', 'description', 'img']