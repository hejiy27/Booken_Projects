# Generated by Django 2.2.8 on 2019-12-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0010_auto_20191211_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='운동설명')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '운동카테고리', 'verbose_name_plural': '운동카테고리'},
        ),
    ]