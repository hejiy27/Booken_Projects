from rest_framework import serializers
from trainer.models import Trainer

class SerializerTrainer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name', 'image_url', 'impact_image_url']