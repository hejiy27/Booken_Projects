from django.db import models

class Trainer(models.Model):
    name = models.CharField(verbose_name='이름', max_length=255)
    image_url = models.ImageField(verbose_name= '트레이너 이미지',blank=True, upload_to= 'trainer/teacher')

    def __str__(self):
        return self.name럇