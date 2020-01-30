from django.db import models

from trainer.models import Trainer

# __all__ : 모듈의 리스트, 즉 모델의 모든 모듈을 import시킨다.
__all__ = ['Exercise', 'ExerciseImage','ExerciseCategory', 'ExerciseDescriptions']

def image_file_name(instance, filename):
    return "/".join(["trainers",instance.trainer.name, "exercise",filename])


class ExerciseCategory(models.Model):
    name = models.CharField(verbose_name='운동 카테고리', max_length=255)
    description = models.TextField(verbose_name='설명',blank=True)

    def __str__(self):
        return f"운동 카테고리: {self.name}"

    class Meta:
        db_table: "booken_category"
        verbose_name = "운동카테고리"
        verbose_name_plural = "운동카테고리들"


class Exercise(models.Model):
    category = models.ForeignKey(ExerciseCategory,verbose_name='운동카테고리',on_delete= models.CASCADE)
    name = models.CharField(verbose_name='운동이름', max_length=255)
    english_name = models.CharField(verbose_name='영어이름', max_length=255)
    time = models.IntegerField(verbose_name='시간', null=True)
    calorie = models.IntegerField(verbose_name='칼로리', blank = True, null=True)

    power_size = (
        ('W', '약함'),
        ('N', '중간'),
        ('S', '강함'))

    power = models.CharField(verbose_name='운동강도', max_length=255, choices=power_size,blank = True, null=True)

    def __str__(self):
        return f"운동 : {self.name}, 칼로리: {self.calorie}"

    class Meta:
        db_table: 'booken_exercise'
        verbose_name = '운동'
        verbose_name_plural = '운동들'


class ExerciseImage(models.Model):
    image_number = models.IntegerField(verbose_name='운동이미지순서')
    exe_image = models.ImageField(verbose_name='운동이미지',upload_to='image_file_name')
    exe_trainer = models.ForeignKey(Trainer,verbose_name='트레이너',on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"운동이미지 {self.image_number}"

    class Meta:
        db_table: 'booken_ex_image'
        verbose_name = '운동이미지'
        verbose_name_plural = '운동이미지'

class ExerciseDescriptions(models.Model):
    number = models.IntegerField(verbose_name='운동번호')
    ex_description = models.TextField(verbose_name='운동설명')
    exercise = models.ForeignKey(Exercise, on_delete= models.CASCADE)


    def __str__(self):
        return f"운동설명{self.number}"

    class Meta:
        db_table: 'booken_description'
        verbose_name = '운동설명'
        verbose_name_plural = '운동설명'

