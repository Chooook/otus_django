from django.shortcuts import render
from .models import Equipment


def equipment_list_view(request):
    equipment_list = Equipment.objects.all()
    context = {
        'equipment_list': equipment_list,
    }
    return render(request, 'equipment/equipment_list.html', context)
