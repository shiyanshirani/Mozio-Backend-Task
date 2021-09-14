# Generated by Django 3.2.7 on 2021-09-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_polygonarea_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="polygonarea",
            name="price",
            field=models.DecimalField(decimal_places=8, default=0.0, max_digits=12),
        ),
    ]
