# Generated by Django 3.2.3 on 2021-10-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('result', models.CharField(max_length=20)),
                ('confidence', models.FloatField()),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Image_Vehicle',
        ),
    ]