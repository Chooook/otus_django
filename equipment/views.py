from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView)

from .models import Category, Equipment


def equipment_view(request):
    equipment_list = Equipment.objects.all()
    context = {
        'equipment_list': equipment_list,
        # 'equipment_count': equipment_list.count(),
    }
    return render(request, 'equipment/equipment_list.html', context)


class AboutTemplateView(TemplateView):
    template_name = 'equipment/about.html'


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('equipment:category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('equipment:category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('equipment:category-list')
