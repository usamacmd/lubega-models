from django.contrib import admin

from .models import EquipmentCategory

class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display= ('category_name', 'date_created', )
    list_filter= ('date_created')
    search_fields= ('category_name', 'products, ProductsAdmin', 'Transaction, TransacctionAdmin')
admin.site.register(EquipmentCategory, EquipmentCategoryAdmin)
#admin.site.register(Products, ProductsAdmin)
#admin.site.register(Transactions, TransactionsAdmin)