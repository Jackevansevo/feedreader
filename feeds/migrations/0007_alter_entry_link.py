# Generated by Django 4.0.6 on 2022-07-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0006_alter_feed_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="link",
            field=models.URLField(max_length=300),
        ),
    ]
