# Generated by Django 3.2.6 on 2021-08-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210810_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainsitemodels',
            name='youtube_silka',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
