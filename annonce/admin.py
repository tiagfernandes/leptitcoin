from django.contrib import admin
from .models import Annonces, Categorie


# Register your models here.

admin.site.register(Categorie)
admin.site.register(Annonces)
