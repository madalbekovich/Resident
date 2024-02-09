from django.urls import path
from .views import LocationView, LocationDetailView

urlpatterns = [
    path('loc1/', LocationView.as_view(), name='api'),
    path('loc2/', LocationDetailView.as_view(), name='api1')
]