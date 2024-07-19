from rest_framework import serializers

from .models import Shop, City, Street


class ShopSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Shop
    #     fields = "__all__"
    street_name = serializers.CharField(source="street.name")
    city_name = serializers.CharField(source="street.city.name")

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "street_name",
            "city_name",
            "opening_time",
            "closing_time",
        ]

    def create(self, validated_data):
        return Shop(**validated_data)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = "__all__"
