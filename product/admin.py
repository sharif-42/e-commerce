from django.contrib import admin
from product.models.product import Product
from .models.product_type import ProductType
from .models.product_group import ProductGroup
from .models.product_brand import ProductBrand
from .models.prouct_color_option import ProductColor
from common.admin import ReadOnlyAdmin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_group', 'product_type', 'brand', 'unit', 'is_serviceable')


@admin.register(ProductType)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available')


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available')


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available')


@admin.register(ProductColor)
class ProductColorAdmin(ReadOnlyAdmin):
    list_display = ('color_code', 'is_available')
    list_filter = ('is_available',)

    fieldsets = (
        (None, {'fields': ('uuid', 'color_code', 'is_available')}),
        ('Additional Fields', {'fields': ('created_by', 'updated_by')}),
        ('Important dates', {'fields': ('created_at', 'updated_at',)}),
    )
