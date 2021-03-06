# Generated by Django 3.0 on 2019-12-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_exercise_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='운동이름')),
                ('english_name', models.CharField(max_length=255, verbose_name='영어이름')),
                ('time', models.IntegerField(blank=True, verbose_name='시간')),
                ('calorie', models.IntegerField(blank=True, verbose_name='칼로리')),
                ('power', models.CharField(blank=True, max_length=255, verbose_name='운동강도')),
                ('descriptions', models.TextField(null=True, verbose_name='운동설명')),
            ],
        ),
    ]
