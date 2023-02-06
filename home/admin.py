from django.contrib import admin
from .models import Homepage_themes, FHHomepage_themes, FBDHomepage_themes, FCDHomepage_themes
from django.contrib.auth.models import User, Group


# class PostAdminSite(admin.AdminSite):
#     list_display = ('Theme_name', 'Theme_price', 'Theme_discount','Theme_url','Theme_category')
#     list_filter = ("Theme_category",)
#     search_fields = ['Theme_name']
#     prepopulated_fields = {'Theme_url': ('Theme_name',)}

class DashboardA(admin.ModelAdmin):
    list_display = ('Theme_name', 'Theme_price', 'Theme_discount','Theme_url','Theme_category')
    list_filter = ("Theme_category",)
    search_fields = ['Theme_name']
    prepopulated_fields = {'Theme_url': ('Theme_name',)}

admin.site.register(Homepage_themes, DashboardA)
admin.site.register(FHHomepage_themes, DashboardA)
admin.site.register(FBDHomepage_themes,DashboardA)
admin.site.register(FCDHomepage_themes,DashboardA)

# FHadmin = PostAdminSite(name = 'fhadmin')djang
# FHadmin.register(FHHomepage_themes, DashboardA)
