# Generated by Django 3.2.3 on 2021-10-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_delete_image_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]