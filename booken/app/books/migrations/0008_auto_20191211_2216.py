# Generated by Django 2.2.8 on 2019-12-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20191206_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '책들', 'verbose_name_plural': '책들'},
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image_url',
            field=models.ImageField(upload_to='book/sign', verbose_name='커버이미지'),
        ),
    ]
