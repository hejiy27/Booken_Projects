from django.contrib import admin

from .models import Exercise, ExerciseCategory,  ExerciseImage

@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    pass

class ExerciseImageAdmin(admin.StackedInline):
    model = ExerciseImage

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    inlines = [ExerciseImageAdmin]

