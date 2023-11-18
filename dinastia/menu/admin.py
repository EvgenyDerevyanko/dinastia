from django.contrib import admin
from menu.models import Product, Category

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'discription', 'category', 'image']
    #list_display_links = None
    list_filter = ['name']
    list_editable = ['price', 'discription', 'category', 'image']
    

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    #list_display_links = None
    list_filter = ['name']
    #list_editable = ['name']

