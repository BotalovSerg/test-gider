from django.contrib import admin

from .models import Shop, City, Street


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "city",
        "street",
        "house",
        "opening_time",
        "closing_time",
    ]
    list_display_links = ["id", "name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "city"]
