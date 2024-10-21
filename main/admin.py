from django.contrib import admin
from .models import Type


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name','sort_order', 'active')
    search_fields = ['name', 'active']        

admin.site.register(Type, TypeAdmin)

