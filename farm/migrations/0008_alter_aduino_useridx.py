# Generated by Django 4.1.1 on 2022-10-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farm", "0007_alter_aduino_devicer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aduino", name="useridx", field=models.IntegerField(null=True),
        ),
    ]