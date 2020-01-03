from rest_framework import serializers
from exercise.models import Category,ExerciseDescriptions,ExerciseImage,Exercise

class SnippetSerializerCategory(serializers.ModelSerializer):
    class Meta:
        module = Category
        fields = ['name', 'description']

class SnippetSerializerExerciseDescrions(serializers.ModelSerializer):
    class Meta:
        module = ExerciseDescriptions
        fields = ['number','ex_description']

class SnippetSerializerExerciseImage(serializers.ModelSerializer):
    class Meta:
        module = ExerciseImage
        fields = ['image_numder', 'exe_image', 'exe_trainer']

class SnippetSerializerExercise(serializers.ModelSerializer):
    class Meta:
        module = Exercise
        fields = ['catgory', 'name', 'english_name', 'time', 'calorie', 'power_size', 'power', 'description' ]

