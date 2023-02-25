import time

from .models import Equipment


def add_value_to_equipment_item_types(value):
    time.sleep(10)
    equipments = Equipment.objects.all()
    for equipment in equipments:
        equipment.item_type += value
        equipment.save()
    return 'Done'
