from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name='저자 명', max_length=255)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(verbose_name='출판사 명', max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(verbose_name = '이름', max_length= 255)
    isbn = models.CharField(verbose_name= 'ISBN', max_length= 255)
    weight = models.IntegerField(verbose_name= '무게', blank= True)
    page = models.IntegerField(verbose_name= '페이지',blank=True)
    sale_price = models.IntegerField(verbose_name='판매가격', blank=True)
    used_price = models.IntegerField(verbose_name= '중고가격', blank=True)

    # DecimalField 는 숫자로 받으며, 정수와 소수점 포함 자리수는 5, 소수점 자리 수 2 로 지정
    grade = models.DecimalField(verbose_name='평점', max_digits= 5,decimal_places= 2)
    #cover_image_url = models.ImageField(verbose_name= '커버이미지',blank=True, upload_to= '')

    # author이 삭제될때 Author도 같이 삭제한다. CASCADE
    author = models.ForeignKey(Author,on_delete= models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)