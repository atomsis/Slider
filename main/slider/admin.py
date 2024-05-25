from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderItem

class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail')

    def image_thumbnail(self, obj):
        return obj.image.url if obj.image else ''

    image_thumbnail.short_description = 'Image'

admin.site.register(SliderItem, SliderItemAdmin)
