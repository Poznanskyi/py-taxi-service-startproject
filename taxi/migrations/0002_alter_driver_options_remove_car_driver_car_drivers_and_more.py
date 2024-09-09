# Generated by Django 5.1.1 on 2024-09-09 06:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "driver", "verbose_name_plural": "drivers"},
        ),
        migrations.RemoveField(
            model_name="car",
            name="driver",
        ),
        migrations.AddField(
            model_name="car",
            name="drivers",
            field=models.ManyToManyField(
                related_name="cars", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cars",
                to="taxi.manufacturer",
            ),
        ),
        migrations.RemoveField(
            model_name="driver",
            name="license_number",
        ),
        migrations.AlterModelTable(
            name="car",
            table=None,
        ),
        migrations.AlterModelTable(
            name="manufacturer",
            table=None,
        ),
        migrations.AddField(
            model_name="driver",
            name="license_number",
            field=models.CharField(default="default_value", max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
