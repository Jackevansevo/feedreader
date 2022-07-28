# Generated by Django 4.0.6 on 2022-07-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0013_alter_feed_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='entry',
            constraint=models.UniqueConstraint(fields=('feed', 'guid'), name='duplicate guid'),
        ),
        migrations.AddConstraint(
            model_name='entry',
            constraint=models.UniqueConstraint(fields=('feed', 'link'), name='duplicate link'),
        ),
    ]
