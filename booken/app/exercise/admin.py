from django.contrib import admin
from .models import Exercise, Category


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class ExersisesAdmin(admin.ModelAdmin):
    pass