from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField('タイトル', max_length=255)
    thumbnail = models.ImageField('サムネイル', help_text='幅が4、高さが3の割合で!')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    # 詳細ページでの並びに関する設定
    container_width = models.IntegerField('コンテナの幅', default=900)
    is_auto_order = models.BooleanField('自動並び替え機能を使うか', default=True,
                                        help_text='Falseの場合は必ず順番通に並べられるので、注意しないと歪な見た目になります。')
    column_width = models.IntegerField('1列の幅', default=375)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    src = models.ImageField('サムネイル', help_text='こちらの幅や高さは自由')
    alt = models.CharField('imgのaltテキスト', max_length=255)
    order = models.PositiveIntegerField(default=0)
    width = models.IntegerField('画像幅', default=375)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.alt
