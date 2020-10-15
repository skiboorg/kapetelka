# Generated by Django 3.0.9 on 2020-10-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201014_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.CharField(max_length=255, null=True, verbose_name='Категория товаров'),
        ),
        migrations.AddField(
            model_name='category',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
