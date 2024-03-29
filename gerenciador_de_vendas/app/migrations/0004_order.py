# Generated by Django 4.1 on 2023-06-28 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_products_productscategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("requestDate", models.DateField()),
                ("amount", models.IntegerField(null=True)),
                ("status", models.CharField(max_length=10)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.products"
                    ),
                ),
            ],
        ),
    ]
