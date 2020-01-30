from django.db import models




class Author(models.Model):
    name = models.CharField(verbose_name='저자 명', max_length=255)

    def __str__(self):
        return self.name
    # class Meta:
    #     db_

class Publisher(models.Model):
    name = models.CharField(verbose_name='출판사 명', max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(verbose_name = '이름', max_length= 255)
    isbn = models.CharField(verbose_name= 'ISBN', max_length= 255)
    cover_image_url = models.ImageField(verbose_name='커버이미지', upload_to='book/sign')
    weight = models.IntegerField(verbose_name= '무게', null= True)
    page = models.IntegerField(verbose_name= '페이지',null=True)
    sale_price = models.IntegerField(verbose_name='판매가격', null=True)
    used_price = models.IntegerField(verbose_name= '중고가격', null=True)
    # DecimalField 는 숫자로 받으며, 정수와 소수점 포함 자리수는 5, 소수점 자리 수 2 로 지정
    grade = models.DecimalField(verbose_name='평점', max_digits= 5,decimal_places= 2)
     # author이 삭제될때 Author도 같이 삭제한다. CASCADE
    author = models.ForeignKey(Author,on_delete= models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table: 'booken_books'
        verbose_name = '책들'
        verbose_name_plural = '책들'