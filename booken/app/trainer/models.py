from django.db import models

class Trainer(models.Model):
    name = models.CharField(verbose_name='이름', max_length=255)
    image_url = models.ImageField(verbose_name= '트레이너 이미지',blank=True, upload_to= 'trainer/teacher')
    impact_image_url =models.ImageField(verbose_name='트레이너 선택 이미지',blank=True, upload_to='trainer/teacher2')

    def __str__(self):
        return self.name

    class Meta:
        db_table: 'booken_tainer'
        verbose_name = '트레이너들'
        verbose_name_plural = '트레이너들'