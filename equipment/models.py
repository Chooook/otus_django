from django.db import models


class TimestampMixin(models.Model):

    class Meta:
        abstract = True

    create = models.DateTimeField(name='created_at', auto_now_add=True)
    update = models.DateTimeField(name='updated_at', auto_now=True)


class Supplier(TimestampMixin):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name


class Category(TimestampMixin):
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    cost = models.PositiveIntegerField(default=0)
    product_name = models.CharField(unique=True, max_length=64)
    supplier = models.ManyToManyField(Supplier)


class Equipment(Product, TimestampMixin):

    class Meta:
        unique_together = ('name', 'category')

    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image can be blob (for desktop app) or on disk (for server app - faster)
    img = models.ImageField(upload_to='equipment', blank=True, null=True)

    def __str__(self):
        return self.name

    def buy(self):
        print('something')


# proxy table example with another (extended?) functionality
class DebugEquipment(Equipment):

    class Meta:
        proxy = True

    def buy(self):
        print('something before')
        super().buy()
