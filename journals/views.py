from rest_framework.generics import ListAPIView
from .models import Location, LocationDetail
from .serializer import LocationSerializer, LocationDetailSerializer


class LocationView(ListAPIView):
    queryset = Location.objects.all().order_by('?')
    serializer_class = LocationSerializer

class LocationDetailView(ListAPIView):
    queryset = Location.objects.all().order_by('?')
    serializer_class = LocationSerializer