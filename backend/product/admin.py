from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Product, ProductTag
# Register your models here.


class ProductTagAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "category"
    list_display = (
        'tree_actions', 'indented_title', 'related_products_count',
        'related_products_cumulative_count'
    )
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = ProductTag.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative = True
        )
        
        qs = ProductTag.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative = False
        )
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related product (for this specific tag)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related product (in tree)'

class productAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_owner', 'product_image']
    list_filter = ['product_owner', 'category']
    search_fields = ['product_name', 'product_owner']

admin.site.register(ProductTag, ProductTagAdmin)
admin.site.register(Product, productAdmin)
