# Generated by Django 3.0.8 on 2020-07-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_auto_20200711_0953"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="upvotes_amount",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
