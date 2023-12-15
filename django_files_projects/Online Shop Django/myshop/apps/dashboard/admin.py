from django.contrib import admin
from apps.dashboard.models import  ProductModel

admin.site.site_header="Electron Shop"


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'slug', 'price',
    'available', 'created', 'updated']

    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('product_name',)}