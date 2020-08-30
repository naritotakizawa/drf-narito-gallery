from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 5
    fields = ('preview', 'src', 'width', 'alt')
    readonly_fields = ('preview',)

    def preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:100px;">'.format(obj.src.url))


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
