# Generated by Django 3.2.6 on 2021-08-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20210817_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futuremodels',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
