from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from transliterate import translit


class Product(models.Model):
    name = models.CharField('Название', max_length=150, db_index=True)
    slug = models.SlugField('URL', unique=True, db_index=True)
    image = models.ImageField('Изображение', upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField('Описание', blank=True)
    price = models.PositiveIntegerField('Цена')
    available = models.BooleanField('В наличии', default=True)
    stock = models.PositiveIntegerField('Кол-во')
    create_time = models.DateTimeField('Время создания', auto_now_add=True)
    update_time = models.DateTimeField('Время обновления', auto_now=True)
    cat = models.ForeignKey('Category', db_index=True, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(str(self.name), 'ru', reversed=True))
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('show_product', kwargs={'cat_slug': self.cat.slug, 'product_slug': self.slug})

    def get_stock_range(self):
        return (i for i in range(1, int(self.stock) + 1))

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-create_time', 'name']
        index_together = (('id', 'slug'),)


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100, db_index=True)
    slug = models.SlugField('URL категории', db_index=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(str(self.name), 'ru', reversed=True))
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('show_cat', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
