# Generated by Django 4.0.6 on 2022-07-14 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feeds", "0002_alter_entry_unique_together_alter_entry_guid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="slug",
            field=models.SlugField(max_length=300),
        ),
        migrations.AlterField(
            model_name="entry",
            name="title",
            field=models.CharField(max_length=300),
        ),
    ]
