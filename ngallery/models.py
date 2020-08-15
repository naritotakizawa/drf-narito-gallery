from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField('タイトル', max_length=255)
    thumbnail = models.ImageField('サムネイル', help_text='幅が4、高さが3の割合で!')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='タグ')
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    src = models.ImageField('サムネイル', help_text='こちらの幅や高さは自由')
    alt = models.CharField('imgのaltテキスト', max_length=255)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.alt
