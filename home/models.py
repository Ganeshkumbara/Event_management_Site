from django.db import models
from PIL import Image
# Create your models here.


class Homepage_themes(models.Model):
    Theme_name =  models.CharField(max_length=100)
    Theme_price = models.IntegerField()
    Theme_discount = models.IntegerField()
    Theme_offer = models.BooleanField()
    Theme_discription = models.TextField()
    Theme_image = models.ImageField(upload_to='themePic')
    Theme_url = models.SlugField(max_length=40)
    category = [
        ('Bday_Party','Bday_Party'),
        ('Bachelorette','Bachelorette'),
        ('Baby_Shower','Baby_Shower'),
        ('Corporate_party','Corporate_party'),
    ]
    Theme_category = models.CharField(verbose_name='Category', choices=category, max_length=255,)
    