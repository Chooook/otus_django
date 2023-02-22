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
    context_object_name = 'category_list'

    # change output queryset
    # def get_queryset(self):
    #     return self.model.objects.filter(field='value')


class CategoryDetailView(DetailView):
    model = Category

    # def get_queryset(self):
    #     return self.model.objects.filter(field='value')
    #
    # def get_object(self, queryset=None):
    #     return ...
    #
    # add some information to use in template
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['some_key'] = 'some_information'
    #     return context
    # overload GET method (POST overload looks the same)
    # def get(self, request, *args, **kwargs):
    #     add some logging here??
    #     return super().get(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('equipment:category-list')

    # forms overload
    # def form_valid(self, form):
    #     return super().form_valid(form)
    # 
    # def form_invalid(self, form):
    #     return super().form_invalid(form)


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name',)
    success_url = reverse_lazy('equipment:category-list')

    # to get success_url dynamically
    # def get_success_url(self):
    #     return super().get_success_url()


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('equipment:category-list')
