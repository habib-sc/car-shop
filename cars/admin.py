from django.contrib import admin
from django.utils.html import format_html

from .models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'city', 'model', 'body_style', 'color', 'year', 'fuel_type')
    list_filter = ('city', 'model', 'color', 'year', 'fuel_type')


admin.site.register(Car, CarAdmin)
