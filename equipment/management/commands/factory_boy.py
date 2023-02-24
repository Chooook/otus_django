import factory
from django.core.management import BaseCommand
from factory.django import DjangoModelFactory

from equipment.models import Product, Equipment, Supplier, Category


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'cat%d' % n)


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Equipment.objects.all().delete()
        Supplier.objects.all().delete()
        Category.objects.all().delete()

        for _ in range(5):
            ProductFactory()
