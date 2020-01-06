from rest_framework.views import APIView
from rest_framework.response import Response

from trainer.models import Trainer
from trainer.serializers import SerializerTrainer


class TrainerListAPIView(APIView):
    def get(self, request):
        trainer = Trainer.objects.all()
        serializer = SerializerTrainer(trainer,many = True)
        return Response(serializer.data)


