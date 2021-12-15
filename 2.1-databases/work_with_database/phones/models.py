from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50, verbose_name='Модель')
    price = models.IntegerField()
    image = models.CharField(max_length=150)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, db_index=True, verbose_name="URL")
