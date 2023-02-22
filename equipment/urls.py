from django.urls import path

from .views import equipment_view, about_view

app_name = 'equipment'

urlpatterns = [
    path('', equipment_view),
    path('about', about_view),
]
