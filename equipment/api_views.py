from rest_framework import viewsets
from rest_framework import renderers

from .models import Category
from .serializers import CategorySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    # how multiple renderers works???
    renderer_classes = [renderers.JSONRenderer, renderers.AdminRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

