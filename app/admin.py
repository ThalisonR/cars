from django.contrib import admin
from app.models import Car

# Register your models here.

class CarFilter(admin.ModelAdmin):
    list_display = ("id", "brand","model", "year")
    list_display_links = ("id", "brand","model", "year")
    # list_filter = ("brand", "year")  # Caixa de filtros
    search_fields = ("brand", "model")
    
admin.site.register(Car, CarFilter)