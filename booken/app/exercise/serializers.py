from rest_framework import serializers
from exercise.models import Category,ExerciseDescriptions,ExerciseImage,Exercise

class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class SerializerExerciseDescrions(serializers.ModelSerializer):
    class Meta:
        model = ExerciseDescriptions
        fields = ['number','ex_description']

class SerializerExerciseImage(serializers.ModelSerializer):
    class Meta:
        model = ExerciseImage
        fields = ['image_numder', 'exe_image', 'exe_trainer']

class SerializerExercise(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['category', 'name', 'english_name', 'time', 'calorie', 'power_size', 'power', 'description']

