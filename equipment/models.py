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


class Category(models.Model):
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Equipment(models.Model):

    class Meta:
        unique_together = ('type', 'category')

    type = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    def buy(self):
        print('something')


class Product(TimestampMixin):
    name = models.CharField(unique=True, max_length=64)
    type = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    suppliers = models.ManyToManyField(Supplier)
    cost = models.PositiveIntegerField(default=0)
    # image can be blob (for desktop app) or on disk (for server app - faster)
    img = models.ImageField(upload_to='product', blank=True, null=True)


# proxy table example with another (extended?) functionality
class DebugEquipment(Equipment):

    class Meta:
        proxy = True

    def buy(self):
        print('something before')
        super().buy()
