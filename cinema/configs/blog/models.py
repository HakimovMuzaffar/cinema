from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150,
                             unique=True,
                             verbose_name='Name of category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Name of cinema')
    image = models.ImageField(upload_to='photos_cinema/', null=True, blank=True, verbose_name='Pictures')
    view = models.IntegerField(default=0, verbose_name='Views')
    description = models.TextField(verbose_name='Content')
    publish = models.BooleanField(default=True, verbose_name='Publish')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created cinema')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update cinema')
    rating = models.FloatField(verbose_name='Rating of cinema')

    def get_photo(self):
        if self.image:
            return self.image.url
        else:
            return 'https://www.gkb1.ru/upload/no_image.png'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
