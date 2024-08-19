from django.contrib import admin
from .models import Category
from .models import Item
admin.site.register(Category)
class ItemAdmin(admin.ModelAdmin):
    exclude = ('slug',)  # Excludes the slug field from the admin form

admin.site.register(Item, ItemAdmin)