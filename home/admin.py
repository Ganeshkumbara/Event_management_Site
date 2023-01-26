from django.contrib import admin
from .models import Homepage_themes
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('Theme_name', 'Theme_price', 'Theme_discount','Theme_url','Theme_category')
    list_filter = ("Theme_name",)
    search_fields = ['Theme_name', 'Theme_price']
    prepopulated_fields = {'Theme_url': ('Theme_name',)}

admin.site.register(Homepage_themes, PostAdmin)