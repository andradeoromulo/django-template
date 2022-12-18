from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'created_at')
    list_display_links = ('id', 'code')
    search_fields = ('code', 'name')
    readonly_fields = ('created_at',)
    list_per_page = 20

admin.site.register(Product, ProductAdmin)