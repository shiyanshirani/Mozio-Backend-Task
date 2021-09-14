from django.db import models

# Create your models here.

LANGUAGE_CHOICES = [
    ("ENG", "English"),
    ("SPA", "Spanish"),
    ("CHI", "Chinese"),
    ("FRA", "French"),
    ("GER", "German"),
    ("HIN", "Hindi"),
    ("JPN", "Japanese"),
    ("AR", "Arabic"),
]

CURRENCY_CHOICES = [
    ("INR", "India Ruppee"),
    ("USD", "United States Dollar"),
    ("YEN", "Japanese Yen"),
    ("EUR", "EURO"),
    ("GBP", "Pound"),
]


class Provider(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.name


class PolygonArea(models.Model):
    provider_name = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="provider"
    )
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=12, decimal_places=8, default=0.0000)
    geojson = models.TextField()

    def __str__(self):
        return self.name
