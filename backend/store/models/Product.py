from django.db import  models
from .Category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    stock = models.PositiveIntegerField(null=False, blank=False, default=0)
    price = models.IntegerField(null=False, blank=False, default=0)
    description = models.TextField(null=False, blank=False, default='')

    # image = models.ImageField(null=False, blank=False, default='default.jpg')

    def __Str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
