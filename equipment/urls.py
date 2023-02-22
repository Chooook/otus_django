from django.urls import path

from . import views

app_name = 'equipment'

urlpatterns = [
    path('', views.equipment_view, name='equipment'),
    path('about', views.about_view, name='about'),
    path('category/list',
         views.CategoryListView.as_view(),
         name='category-list'),
]
