from django.utils import timezone
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .models import Shop, City, Street
from .serializers import ShopSerializer, CitySerializer, StreetSerializer


class CityApiView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs.get("city_id")
        return Street.objects.filter(city_id=city_id)


class ShopApiView(generics.ListCreateAPIView):
    # queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        queryset = Shop.objects.all()
        street_name = self.request.query_params.get('street', None)
        city_name = self.request.query_params.get('city', None)
        open_status = self.request.query_params.get('open', None)

        if street_name:
            queryset = queryset.filter(street__name__icontains=street_name)
        if city_name:
            queryset = queryset.filter(street__city__name__icontains=city_name)
        if open_status is not None:
            current_time = timezone.localtime(timezone.now()).time()
            if open_status == '1':
                queryset = queryset.filter(opening_time__lte=current_time, closing_time__gte=current_time)
            elif open_status == '0':
                queryset = queryset.exclude(opening_time__lte=current_time, closing_time__gte=current_time)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # shop = serializer.save()
        # headers = self.get_success_headers(serializer.data)
        self.perform_create(serializer)
        return Response(
            {"id": serializer.data["id"]}, status=status.HTTP_201_CREATED
        )
