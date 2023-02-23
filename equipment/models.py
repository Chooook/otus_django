from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return self.name


class Equipment(models.Model):

    class Meta:
        unique_together = ('name', 'category')

    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image can be blob (for desktop app) or on disk (for server app - faster)
    img = models.ImageField(upload_to='equipment', blank=True, null=True)

    def __str__(self):
        return self.name
