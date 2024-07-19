from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)
    opening_time = models.TimeField(blank=True)
    closing_time = models.TimeField(blank=True)
    street = models.ForeignKey("Street", related_name='shops', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey("City", related_name='streets', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
