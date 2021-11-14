from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField(help_text="How many items are currently in stock.")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default="", blank=True)
    sku = models.CharField(max_length=20, unique=True, verbose_name="Stock Keeping Unit")
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100)
    product = models.ManyToManyField("Product", related_name='categories')

    def __str__(self):
        return f'{self.name}'


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.image}'
