from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

from . import views, api_views

app_name = 'equipment'

router = routers.DefaultRouter()
router.register('category', api_views.CategoryModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('',
         views.IndexTemplateView.as_view(),
         name='index'),
    path('about',
         views.AboutTemplateView.as_view(),
         name='about'),
    path('category/create',
         views.CategoryCreateView.as_view(),
         name='category-create'),
    path('category/list',
         views.CategoryListView.as_view(),
         name='category-list'),
    path('category/detail/<int:pk>',
         views.CategoryDetailView.as_view(),
         name='category-detail'),
    path('category/update/<int:pk>',
         views.CategoryUpdateView.as_view(),
         name='category-update'),
    path('category/delete/<int:pk>',
         views.CategoryDeleteView.as_view(),
         name='category-delete'),
    path('equipment/create',
         views.EquipmentCreateView.as_view(),
         name='equipment-create'),
    path('equipment/list',
         views.EquipmentListView.as_view(),
         name='equipment-list'),
    path('equipment/detail/<int:pk>',
         views.EquipmentDetailView.as_view(),
         name='equipment-detail'),
    path('equipment/update/<int:pk>',
         views.EquipmentUpdateView.as_view(),
         name='equipment-update'),
    path('equipment/delete/<int:pk>',
         views.EquipmentDeleteView.as_view(),
         name='equipment-delete'),
    path('equipment/contact',
         views.ContactFormView.as_view(),
         name='contact'),
]

# needed if not production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
