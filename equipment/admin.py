from django.contrib import admin
import django_rq

from .models import Category, Equipment, Product, DebugEquipment, Supplier
from .tasks import add_value_to_equipment_item_types


@admin.action(description='Add value to equipment names')
def add_value(modeladmin, request, queryset):
    queue = django_rq.get_queue()
    queue.enqueue(add_value_to_equipment_item_types, 'some text')


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'display_suppliers')

    def display_suppliers(self, obj):
        suppliers = obj.suppliers.values_list('name', flat=True)
        return '; '.join(suppliers)
    display_suppliers.short_description = 'suppliers'


@admin.register(Equipment)
class EquipmentModelAdmin(admin.ModelAdmin):
    actions = [add_value]


admin.site.register(Category)
# admin.site.register(Equipment)
# admin.site.register(Product, ProductModelAdmin)
admin.site.register(DebugEquipment)
# admin.site.register(Supplier)


# another way to register models to admin
@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    pass
