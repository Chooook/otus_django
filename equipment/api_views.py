from rest_framework import viewsets, renderers, generics, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

# from djangorestframework_camel_case import render

from .models import Category
from .serializers import CategorySerializer
from .filters import CategoryFilter


class CategoryModelViewSet(viewsets.ModelViewSet):
    # how multiple renderers works???
    renderer_classes = [renderers.JSONRenderer, renderers.AdminRenderer]
    # for JavaScript frontend developers comfort
    # renderer_classes = [render.CamelCaseJSONRenderer,
    #                     render.CamelCaseBrowsableAPIRenderer]
    serializer_class = CategorySerializer
    # definition of fields for django-filter
    filterset_fields = ['name']

    # example of filter class usage
    # filterset_class = CategoryFilter

    def get_queryset(self):
        queryset = Category.objects.all()
        # filter queryset according to current user
        # user = self.request.user
        # return Category.objects.filter(purchaser=user)
        #
        # filter queryset according to username from url params
        # you need something like this in urls to use that method
        # path('category/<str:field_name>/', CategoryList.as_view()),
        # field_name = self.kwargs['field_name']
        # filter queryset according to request params
        # field_name = self.request.query_params.get('field_name')
        # return Category.objects.filter(category__field_name=field_name)
        # example of using _lte suffix to get less or equal (_gte, _gt, etc.)
        # numerical_var = self.request.query_params.get('numerical_var')
        # if numerical_var:
        #     queryset = queryset.filter(numerical_field_lte=numerical_var)
        return queryset


# only for create and retrieve ViewSet
class CRCategoryModelViewSet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# analogue to CRCategoryModelViewSet custom ViewSet example
# you are able to use another mixins with GenericViewSet
# to create your own ViewSet as constructor
# ModelViewSet looks like this at fact
# class ModelViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    generics.GenericViewSet):
class CustomCategoryViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,  # detail view
                            viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # you can change definite view with overload of method,
    # method names are corresponding to their view type
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # you can create your own method, and it will be
    # routed by DefaultRouter automatically
    # if you don't need pk definition -> detail=False and no pk in params
    @action(detail=True, methods=['get'])
    def some_another_method(self, request, pk=None):
        first_category = Category.objects.all().first()
        serializer = CategorySerializer(first_category)
        if serializer.data:
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
