from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=55, unique=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    description = models.TextField(max_length=200, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
        
    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])

    class Meta:
        verbose_name_plural = "categories"