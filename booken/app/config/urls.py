"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from books.views import BookListAPIView
from exercise.views import ExerciseListAPIView
from trainer.views import TrainerListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListAPIView.as_view()),
    path('trainer/', TrainerListAPIView.as_view()),
    path('exercise/', ExerciseListAPIView.as_view()),
]


# /media/로 오는 요청은 MEDIA_ROOT의 파일들에서 찾아서 리턴
urlpatterns += static(
    prefix= settings.MEDIA_URL,
    document_root = settings.MEDIA_ROOT,
)