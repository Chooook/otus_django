from django_filters import rest_framework as filters

from .models import Category


class CategoryFilter(filters.FilterSet):
    some_num_filter = filters.NumberFilter('some_num_field', lookup_expr='lte')

    class Meta:
        model = Category
        fields = ['name']
