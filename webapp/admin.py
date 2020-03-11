from django.contrib import admin

from .models import Converter


class ConverterAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'date', 'email']


admin.site.register(Converter, ConverterAdmin)
