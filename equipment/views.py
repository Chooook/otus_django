from django.shortcuts import render
from .models import Equipment


def equipment_view(request):
    equipment_list = Equipment.objects.all()
    context = {
        'equipment_list': equipment_list,
        # 'equipment_count': equipment_list.count(),
    }
    return render(request, 'equipment/equipment.html', context)


def about_view(request):
    return render(request, 'equipment/about.html')
