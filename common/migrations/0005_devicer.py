# Generated by Django 4.1.1 on 2022-10-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0004_alter_customuser_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="devicer",
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
                ("device", models.IntegerField()),
            ],
        ),
    ]