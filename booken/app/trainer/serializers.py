from rest_framework import serializers
from trainer.models import Trainer

class SnippetSerializerTrainer(serializers.ModelSerializer):
    class Meta:
        module = Trainer
        fields = ['name', 'image_url', 'impact_image_url']