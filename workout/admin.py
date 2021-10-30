from django.contrib import admin
from .models import Training, Category, Equipment, Video


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('day_number', 'name', 'duration', 'is_active_day', 'video')
    list_display_links = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_added_to_favourites',)
    list_display_links = ('name',)


admin.site.register(Training, TrainingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Video, VideoAdmin)
