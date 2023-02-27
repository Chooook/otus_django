from rest_framework import viewsets
from rest_framework import renderers
# from djangorestframework_camel_case import render

from .models import Category
from .serializers import CategorySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    # how multiple renderers works???
    renderer_classes = [renderers.JSONRenderer, renderers.AdminRenderer]
    # for JavaScript frontend developers comfort
    # renderer_classes = [render.CamelCaseJSONRenderer,
    #                     render.CamelCaseBrowsableAPIRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

