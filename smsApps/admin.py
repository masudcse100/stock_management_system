from django.contrib import admin

from . models import Categorie
# Register your models here.
@admin.register(Categorie)
class CategorieModelAdmin(admin.ModelAdmin):
    list_display = ['cat_name']