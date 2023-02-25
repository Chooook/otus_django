from django.db import models
from django.utils.functional import cached_property


class TimestampMixin(models.Model):

    class Meta:
        abstract = True

    create = models.DateTimeField(name='created_at', auto_now_add=True)
    update = models.DateTimeField(name='updated_at', auto_now=True)


class Supplier(TimestampMixin):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        verbose_name_plural = 'categories'

    # when use this decorator, method becomes property (use without braces)
    # if data changed after caching (first call of property),
    # property will not change!!!
    @cached_property
    def equipments_count(self):
        equipments_count = Equipment.objects.filter(category=self)
        return equipments_count.count()

    @cached_property
    def has_equipment(self):
        return Equipment.objects.filter(category=self).exists()

    def __str__(self):
        return self.name


class Equipment(models.Model):

    class Meta:
        unique_together = ('item_type', 'category')

    item_type = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_type

    def buy(self):
        print('something')


class Product(TimestampMixin):
    name = models.CharField(unique=True, max_length=64)
    item_type = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    suppliers = models.ManyToManyField(Supplier)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    # image can be blob (for desktop app) or on disk (for server app - faster)
    img = models.ImageField(upload_to='product', blank=True, null=True)


# proxy table example with another (extended?) functionality
class DebugEquipment(Equipment):

    class Meta:
        proxy = True

    def buy(self):
        print('something before')
        super().buy()
