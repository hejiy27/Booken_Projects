# Generated by Django 2.2.8 on 2019-12-11 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_trainer_image_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainer',
            options={'verbose_name': '트레이너들', 'verbose_name_plural': '트레이너'},
        ),
    ]
