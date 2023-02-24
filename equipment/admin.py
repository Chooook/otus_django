from django.contrib import admin
from .models import Category, Equipment, Product, DebugEquipment


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Equipment)
admin.site.register(Product)
admin.site.register(DebugEquipment)
