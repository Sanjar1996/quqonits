# Generated by Django 3.2.6 on 2021-08-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_alter_futuremodels_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainsitemodels',
            name='video',
            field=models.FileField(blank=True, upload_to='upload/'),
        ),
    ]
