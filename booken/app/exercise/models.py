from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='운동 카테고리', max_length=255)
    description = models.CharField(verbose_name='설명', max_length=255)

    def __str__(self):
        return self.name


class Exercise (models.Model):
    name = models.CharField(verbose_name='운동이름', max_length=255)
    english_name = models.CharField(verbose_name='영어이름', max_length=255)
    time = models.IntegerField(verbose_name='시간', blank=True)
    calorie = models.IntegerField(verbose_name='칼로리', blank=True)
    power = models.CharField(verbose_name='운동강도',max_length=255, blank=True)
    descriptions = models.TextField(verbose_name='운동설명',null=True)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    # images = models.ImageField(verbose_name= '운동 이미지',blank=True, upload_to= '')

    def __str__(self):
        return self.name


