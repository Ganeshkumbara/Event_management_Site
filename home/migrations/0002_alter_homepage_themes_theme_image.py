# Generated by Django 4.1.4 on 2023-01-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage_themes',
            name='Theme_image',
            field=models.ImageField(upload_to='themePic'),
        ),
    ]
