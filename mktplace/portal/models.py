from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True,
                               related_name='cat_child')
    order = models.IntegerField(null=True, blank=True)
    hidden = models.BooleanField(default=False)
