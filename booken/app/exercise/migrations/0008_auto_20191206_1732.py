# Generated by Django 3.0 on 2019-12-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0007_auto_20191206_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='calorie',
            field=models.IntegerField(null=True, verbose_name='칼로리'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='time',
            field=models.IntegerField(null=True, verbose_name='시간'),
        ),
    ]
