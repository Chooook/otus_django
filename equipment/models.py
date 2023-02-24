from django.db import models


class TimestampMixin(models.Model):

    class Meta:
        abstract = True

    create = models.DateTimeField(name='created_at', auto_now_add=True)
    update = models.DateTimeField(name='updated_at', auto_now=True)


class Category(TimestampMixin):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.name


class Product(models.Model):
    cost = models.PositiveIntegerField(default=0)
    product_name = models.CharField(unique=True, max_length=64)


class Equipment(Product, TimestampMixin):

    class Meta:
        unique_together = ('name', 'category')

    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image can be blob (for desktop app) or on disk (for server app - faster)
    img = models.ImageField(upload_to='equipment', blank=True, null=True)

    def __str__(self):
        return self.name
