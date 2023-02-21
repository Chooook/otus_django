from django.urls import path

from .views import equipment_list_view

app_name = 'equipment'

urlpatterns = [
    path('', equipment_list_view),
]
