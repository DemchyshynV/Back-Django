from django.db import models


class ProductCategoriesModel(models.Model):
    class Meta:
        db_table = 'product_categories'

    name = models.CharField(unique=True, blank=False, max_length=50)


class SubProductCategoriesModel(models.Model):
    class Meta:
        db_table = 'sub_product_categories'

    categories = models.ForeignKey(ProductCategoriesModel, on_delete=models.CASCADE, related_name='sub_category')
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return f'{self.id} {self.name}'
