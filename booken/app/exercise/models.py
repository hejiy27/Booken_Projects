from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='운동 카테고리', max_length=255)
    description = models.CharField(verbose_name='설명', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table: 'booken_category'
        verbose_name = '운동카테고리'
        verbose_name_plural = '운동카테고리'

class Descriptions(models.Model):
    description = models.TextField(verbose_name='운동설명',null=True)

# 운동 순서 저장하는 필드 만들기!
# 운동이미지 필드 만들기
# -이미지, 순서, 트레이




class Exercise (models.Model):
    name = models.CharField(verbose_name='운동이름', max_length=255)
    english_name = models.CharField(verbose_name='영어이름', max_length=255)
    time = models.IntegerField(verbose_name='시간', null=True)
    calorie = models.IntegerField(verbose_name='칼로리', null=True)
    power = models.CharField(verbose_name='운동강도',max_length=255, blank=True)
    descriptions = models.TextField(verbose_name='운동설명',null=True)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    images = models.ImageField(verbose_name= '운동 이미지',blank=True, upload_to= 'exercise/action')
    description = models.ForeignKey(Descriptions,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table: 'booken_exercise'
        verbose_name = '운동들'
        verbose_name_plural = '운동들'

