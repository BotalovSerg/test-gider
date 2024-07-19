from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=200)
    house = models.CharField(max_length=200)
    opening_time = models.TimeField(blank=True)
    closing_time = models.TimeField(blank=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    street = models.ForeignKey("Street", on_delete=models.CASCADE)

    def is_open(self):
        from django.utils.timezone import now
        current_time = now().time()
        return self.opening_time <= current_time <= self.opening_time

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey("City", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
