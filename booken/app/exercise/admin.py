from django.contrib import admin

from .models import Exercise, Category, ExerciseDescriptions, ExerciseImage

@admin.register(Category)
class ExersisesAdmin(admin.ModelAdmin):
    pass

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(ExerciseDescriptions)
class ExerciseDescriptionsAdmin(admin.ModelAdmin):
    pass

@admin.register(ExerciseImage)
class ExerciseImageAdmin(admin.ModelAdmin):
    pass