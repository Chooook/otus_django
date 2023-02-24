from django.contrib import admin
from .models import Category, Equipment, Product, DebugEquipment, Supplier


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'display_suppliers')


admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(DebugEquipment)
# admin.site.register(Supplier)


# another way to register models to admin
@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    pass
