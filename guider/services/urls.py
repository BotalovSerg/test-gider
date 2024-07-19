from django.urls import path

from . import views

app_name = "services_api"

urlpatterns = [
    path("city/", views.CityApiView.as_view(), name="city"),
    path("city/<int:city_id>/street/", views.StreetViewSet.as_view(), name="all-street-city"),
    path("shop/", views.ShopApiView.as_view(), name="shop"),
]
