# Generated by Django 3.2.7 on 2021-09-13 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210913_1033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Polygon',
            new_name='PolygonArea',
        ),
    ]