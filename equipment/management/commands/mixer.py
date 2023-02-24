from django.core.management import BaseCommand
from mixer.backend.django import mixer

from equipment.models import Product, Equipment, Supplier, Category


class Command(BaseCommand):
    help = 'db fill with mixer'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Equipment.objects.all().delete()
        Supplier.objects.all().delete()
        Category.objects.all().delete()

        for _ in range(5):
            mixer.blend(Product)

        for _ in range(5):
            mixer.blend(Product, type__type='MyEqName')

        for _ in range(5):
            mixer.blend(Product, price=100)
