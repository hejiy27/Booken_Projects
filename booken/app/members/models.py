from django.contrib.auth.models import AbstractUser
from django.db import models

"""custom """


class User(AbstractUser):
    nickname = models.CharField('닉네임', max_length=50, blank=True)
    img_profile = models.ImageField('프로필 이미지', blank=True, upload_to='user/profile')
    attachment = models.FileField('첨부파일', blank=True, upload_to='user/attachment')
