# Generated by Django 3.0.9 on 2020-10-14 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sortitem',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='sortitem',
            name='created',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sortitem',
            name='good_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sortitem',
            name='iid',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Серийный номер'),
        ),
        migrations.AddField(
            model_name='sortitem',
            name='item_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Кол-во товара'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='sort',
        ),
        migrations.AddField(
            model_name='item',
            name='sort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.SortItem', verbose_name='Партия товара'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ItemStatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='sortitem',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Партия товаров'),
        ),
    ]
