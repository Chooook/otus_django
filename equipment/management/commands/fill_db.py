import random

from django.core.management import BaseCommand
from faker import Faker

from equipment.models import Product, Equipment, Supplier, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Equipment.objects.all().delete()
        Supplier.objects.all().delete()
        Category.objects.all().delete()
        faker = Faker()

        for _ in range(10):
            name = faker.unique.name()
            Category.objects.create(name=name)

        categories = Category.objects.all()

        for _ in range(50):
            _type = faker.unique.name()
            category = random.choice(categories)
            Equipment.objects.create(type=_type, category=category)

        equipments = Equipment.objects.all()

        for _ in range(20):
            name = faker.unique.company()
            Supplier.objects.create(name=name)

        suppliers = Supplier.objects.values_list('id', flat=True)

        for _ in range(100):
            name = faker.unique.name()
            _type = random.choice(equipments)
            cost = random.random() * 1000
            description = faker.text()
            prod = Product.objects.create(name=name,
                                          type=_type,
                                          cost=cost,
                                          description=description)
            # not able to add m2m field when creating an instance,
            # so you can use set() or add()
            r_suppliers = random.choices(suppliers, k=random.randint(1, 5))
            prod.suppliers.add(*r_suppliers)
