# Generated by Django 4.1.1 on 2022-10-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farm", "0006_alter_aduino_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aduino", name="devicer", field=models.IntegerField(null=True),
        ),
    ]
