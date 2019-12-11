# Generated by Django 3.0 on 2019-12-07 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField(blank=True)),
                ('pud_date', models.DateField(blank=True, null=True)),
                ('mod_date', models.DateField(blank=True, null=True)),
                ('number_of_comments', models.IntegerField(default=0)),
                ('numder_of_pigbacks', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('authors', models.ManyToManyField(blank=True, to='query.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Blog')),
            ],
        ),
    ]