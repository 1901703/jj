from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_in_category', args=[self.slug])


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='items')
    item_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    item_image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    brand = models.CharField(max_length=100, verbose_name='브랜드', null=True, blank=True)
    item_price = models.IntegerField(verbose_name='상품가격')
    discounted_price = models.IntegerField(verbose_name='할인가격', null=True, blank=True)
    item_amt = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id','slug']]

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.id, self.slug])
