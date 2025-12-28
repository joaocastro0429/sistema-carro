from django.contrib import admin
from .models import Car,Brand

# Register your models here.

class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(Car, carAdmin)
admin.site.register(Brand, BrandAdmin)