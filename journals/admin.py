from django.contrib import admin
from .models import Location, LocationDetail, LocationImg


class LocationImgAdmin(admin.TabularInline):
    model = LocationImg
    extra = 0

class LocationDetailAdmin(admin.StackedInline):  # Adjusted inheritance to StackedInline
    model = LocationDetail
    inlines = [
        LocationImgAdmin
    ]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        LocationDetailAdmin
    ]

admin.site.register(Location, LocationAdmin)