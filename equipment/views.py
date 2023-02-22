from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from .models import Category, Equipment


def equipment_view(request):
    equipment_list = Equipment.objects.all()
    context = {
        'equipment_list': equipment_list,
        # 'equipment_count': equipment_list.count(),
    }
    return render(request, 'equipment/equipment.html', context)


def about_view(request):
    return render(request, 'equipment/about.html')


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('equipment:category-list')
