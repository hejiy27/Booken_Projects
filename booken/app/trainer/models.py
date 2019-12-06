from django.db import models

class Trainer(models.Model):
    name = models.CharField(verbose_name='이름', max_length=255)
    # image_url = models.ImageField(verbose_name='이미지',upload_to=)