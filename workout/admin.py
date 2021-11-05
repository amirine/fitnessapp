from django.contrib import admin

from .models import Training, Category, Equipment, Exercise


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'created_at')
    list_display_links = ('name',)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'repetitions')
    list_display_links = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Training, TrainingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Exercise, ExerciseAdmin)
