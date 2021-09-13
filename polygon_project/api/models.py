from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    language = models.CharField(max_length=150)
    currency = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"
