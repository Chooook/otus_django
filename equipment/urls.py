from django.urls import path

from . import views

app_name = 'equipment'

urlpatterns = [
    path('',
         views.IndexTemplateView.as_view(),
         name='equipment-list'),
    path('equipment-list',
         views.EquipmentListView.as_view(),
         name='equipment-list'),
    path('about',
         views.AboutTemplateView.as_view(),
         name='about'),
    path('category/list',
         views.CategoryListView.as_view(),
         name='category-list'),
    path('category/detail/<int:pk>',
         views.CategoryDetailView.as_view(),
         name='category-detail'),
    path('category/create',
         views.CategoryCreateView.as_view(),
         name='category-create'),
    path('category/update/<int:pk>',
         views.CategoryUpdateView.as_view(),
         name='category-update'),
    path('category/delete/<int:pk>',
         views.CategoryDeleteView.as_view(),
         name='category-delete'),
]
