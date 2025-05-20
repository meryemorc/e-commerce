from django.contrib import admin

# Register your models here.

from . models import Category, Product

@admin.register(Category)
class Category(admin.ModelAdmin):

    prepopulated_fields = {'slug':('name', )}

@admin.register(Product)
class Category(admin.ModelAdmin):

    prepopulated_fields = {'slug':('title',)}