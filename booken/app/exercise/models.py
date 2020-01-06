from django.db import models

from trainer.models import Trainer


class Category(models.Model):
    name = models.CharField(verbose_name='운동 카테고리', max_length=255)
    description = models.CharField(verbose_name='설명', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table: 'booken_category'
        verbose_name = '운동카테고리'
        verbose_name_plural = '운동카테고리'


class ExerciseDescriptions(models.Model):
    number = models.IntegerField(verbose_name='운동설명번호',null=False, default=1)
    ex_description = models.TextField(verbose_name='운동설명')

# # 운동설명이
    def __str__(self):
        return self.number

    class Meta:
        db_table: 'booken_description'
        verbose_name = '운동설명'
        verbose_name_plural = '운동설명'


class ExerciseImage(models.Model):
    image_number = models.IntegerField(verbose_name='운동이미지번호',)
    exe_image = models.ImageField(verbose_name='운동이미지',upload_to='exercise/action')
    exe_trainer = models.ForeignKey(Trainer,verbose_name='트레이너',on_delete=models.CASCADE)

    def __str__(self):
        return self.exe_trainer.name

    class Meta:
        db_table: 'booken_ex_image'
        verbose_name = '운동이미지'
        verbose_name_plural = '운동이미지'


class Exercise (models.Model):
    category = models.ForeignKey(Category,verbose_name='운동카테고리',on_delete= models.CASCADE)
    name = models.CharField(verbose_name='운동이름', max_length=255)
    english_name = models.CharField(verbose_name='영어이름', max_length=255)
    time = models.IntegerField(verbose_name='시간', null=True)
    calorie = models.IntegerField(verbose_name='칼로리', null=True)

    power_size = (
        ('W', '약함'),
        ('N', '중간'),
        ('S', '강함'))
    power = models.CharField(verbose_name='운동강도', max_length=1, choices=power_size)
    # ex_image = models.ForeignKey(ExerciseImage, verbose_name='운동이미지', on_delete=models.CASCADE)

    description = models.ForeignKey(ExerciseDescriptions,verbose_name='운동설명',on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.name

    class Meta:
        db_table: 'booken_exercise'
        verbose_name = '운동들'
        verbose_name_plural = '운동들'

