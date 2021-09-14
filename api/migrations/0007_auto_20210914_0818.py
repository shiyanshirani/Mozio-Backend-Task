# Generated by Django 3.2.7 on 2021-09-14 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_polygonarea_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="polygonarea",
            name="provider_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="provider",
                to="api.provider",
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="currency",
            field=models.CharField(
                choices=[
                    ("INR", "India Ruppee"),
                    ("USD", "United States Dollar"),
                    ("YEN", "Japanese Yen"),
                    ("EUR", "EURO"),
                    ("GBP", "Pound"),
                ],
                max_length=3,
            ),
        ),
    ]
