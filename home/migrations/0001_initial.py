# Generated by Django 4.1.4 on 2023-01-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage_themes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Theme_name', models.CharField(max_length=100)),
                ('Theme_price', models.IntegerField()),
                ('Theme_discount', models.IntegerField()),
                ('Theme_offer', models.BooleanField()),
                ('Theme_discription', models.TextField()),
                ('Theme_image', models.ImageField(upload_to='theme_pic')),
            ],
        ),
    ]
