from rest_framework.response import Response
from rest_framework.views import APIView

from exercise.models import Exercise
from exercise.serializers import SerializerExercise


class ExerciseListAPIView(APIView):
    def get(self,request):
        exercise = Exercise.objects.all()
        serializers = SerializerExercise(exercise,many=True)
        return Response(serializers.data)