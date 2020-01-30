from rest_framework import serializers
from exercise.models import ExerciseCategory,ExerciseDescriptions,ExerciseImage,Exercise



class SerializerExerciseCategory(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCategory
        fields = ["name", "description"]

class SerializerExerciseDescrions(serializers.ModelSerializer):
    class Meta:
        model = ExerciseDescriptions
        fields = ['ex_description']

class SerializerExerciseImage(serializers.ModelSerializer):
    class Meta:
        model = ExerciseImage
        fields = ["url"]

class SerializerExercise(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['category', 'name', 'english_name', 'time', 'calorie', 'power_size', 'power', 'description']

