from django.contrib import admin
from .models import Customer, SellerTags, Seller
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
class SellerTagAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "tag"
    list_display = (
        'tree_actions', 'indented_title', 'related_products_count',
        'related_products_cumulative_count'
    )
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = SellerTags.objects.add_related_count(
            qs,
            Seller,
            'tag',
            'products_cumulative_count',
            cumulative = True
        )
        
        qs = SellerTags.objects.add_related_count(
            qs,
            Seller,
            'tag',
            'products_count',
            cumulative = False
        )
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related seller (for this specific tag)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related seller (in tree)'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user', 'first_name', 'last_name')
    search_fields = ['user', 'first_name',]

class SellerAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_joined',]
    list_filter = ['user', 'date_joined',]
    search_fields = ['user',]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(SellerTags, SellerTagAdmin)