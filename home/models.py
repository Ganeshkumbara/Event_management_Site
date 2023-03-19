from django.db import models
# from .views import clone
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
    Theme_region = models.CharField(max_length=100,default='Home')
    




class FHHomepage_themes(models.Model):
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
    Theme_category = models.CharField(verbose_name='Category', choices=category, max_length=254,)
    Theme_region = models.CharField(max_length=100,default='Hyderabad')

class FBDHomepage_themes(models.Model):
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
    Theme_category = models.CharField(verbose_name='Category', choices=category, max_length=253,)
    Theme_region = models.CharField(max_length=100,default='Bangalore')
    # class Meta: #
    #     ordering = ['-Theme_name']

    # def save(self):
    #     self.Theme_name = '1'+self.Theme_name
    #     super(FBDHomepage_themes, self).save()
    
    # def clone(self):
    #     self.Theme_name = '1'+self.Theme_name
    #     save.()


class FCDHomepage_themes(models.Model):
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
    Theme_category = models.CharField(verbose_name='Category', choices=category, max_length=253,)
    Theme_region = models.CharField(max_length=100,default='Chennai')

class Basemodel(models.Model):
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
    Theme_category = models.CharField(verbose_name='Category', choices=category, max_length=253,)
    Theme_region = models.CharField(max_length=100,default='Chennai')

    class Meta:
        abstract = True

class Test(Basemodel):
    pass

class Test2(Basemodel):
    def __init__(self):
        self.Theme_region = models.CharField(max_length=100,default='world')



# basemodel = Homepage_themes.objects.all()
# for modelz in basemodel:
#     clonemodel = FCDHomepage_themes(Theme_name = modelz.Theme_name, Theme_price=modelz.Theme_price, Theme_discount=modelz.Theme_discount, Theme_offer=modelz.Theme_offer, Theme_discription=modelz.Theme_discription, Theme_image=modelz.Theme_image, Theme_url=modelz.Theme_url, Theme_category=modelz.Theme_category)