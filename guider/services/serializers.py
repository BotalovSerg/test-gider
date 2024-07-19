from rest_framework import serializers

from .models import Shop, City, Street


class ShopSerializer(serializers.ModelSerializer):
    street_name = serializers.CharField(source='street.name')
    city_name = serializers.CharField(source='street.city.name', read_only=True)

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "city_name",
            "street_name",
            "house_number",
            "opening_time",
            "closing_time",
        ]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = "__all__"
