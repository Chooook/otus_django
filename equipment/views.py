from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView,
                                  FormView)

from .forms import CategoryForm, EquipmentForm, ContactForm
from .models import Category, Equipment, Product


class IndexTemplateView(TemplateView):
    template_name = 'equipment/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'equipment/about.html'


class EquipmentCreateView(CreateView):
    model = Equipment
    success_url = reverse_lazy('equipment:equipment-list')
    form_class = EquipmentForm


class EquipmentListView(ListView):
    model = Equipment
    context_object_name = 'equipment_list'


class EquipmentDetailView(DetailView):
    model = Equipment


class EquipmentUpdateView(UpdateView):
    model = Equipment
    success_url = reverse_lazy('equipment:equipment-list')
    form_class = EquipmentForm


class EquipmentDeleteView(DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment:equipment-list')


class CategoryCreateView(CreateView):
    model = Category
    success_url = reverse_lazy('equipment:category-list')
    form_class = CategoryForm

    # forms overload
    # def form_valid(self, form):
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     return super().form_invalid(form)


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


class CategoryUpdateView(UpdateView):
    model = Category
    success_url = reverse_lazy('equipment:category-list')
    form_class = CategoryForm

    # to get success_url dynamically
    # def get_success_url(self):
    #     return super().get_success_url()


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('equipment:category-list')


class ContactFormView(FormView):
    template_name = 'equipment/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('equipment:contact')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product

    # TODO create CRUD, templates and urls for Product
    # optimises query if you use also category output in template??
    def get_queryset(self):
        # if without select_related(), it will load product object and
        # then type(equipment) object, so it's SQL+1 problem in such queries
        # usable with foreign keys
        # return Product.objects.select_related('type')
        # with prefetch_related() it also loads all suppliers to join them
        # to products, but not query for each product to load his suppliers
        # usable with m2m fields
        return (Product.objects
                .select_related('type')
                .prefetch_related('suppliers'))
