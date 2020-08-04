# Generated by Django 3.0.9 on 2020-08-03 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название категории')),
                ('image', models.ImageField(null=True, upload_to='category/images/', verbose_name='Изображение (xxx x xxx)')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('video_file', models.FileField(max_length=255, null=True, upload_to='', verbose_name='Видео локальный файл')),
                ('video_url', models.CharField(max_length=255, null=True, verbose_name='Видео ссылка')),
                ('image', models.ImageField(null=True, upload_to='item/images/', verbose_name='Изображение (xxx x xxx)')),
                ('is_new', models.BooleanField(default=False, verbose_name='Новинка ?')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='api.Category', verbose_name='Относится')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDifficult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название уровня сложности')),
                ('level', models.IntegerField(default=1, verbose_name='Уровень сложности (Цифра)')),
            ],
        ),
        migrations.CreateModel(
            name='ItemLegend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название условного обозначения')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Значение')),
            ],
        ),
        migrations.CreateModel(
            name='ItemMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Значение')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Верхний текст раздела практические рекомендации')),
                ('bottom_text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Нижний текст раздела практические рекомендации')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_recomendations', to='api.Item', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationBlockA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('top_text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Верхний текст раздела')),
                ('bottom_text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Нижний текст раздела')),
                ('image', models.ImageField(null=True, upload_to='item/sub_block_a/images/', verbose_name='Изображение (xxx x xxx)')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recomendation_blocks_a', to='api.Item', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationBlockB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('top_text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Верхний текст раздела')),
                ('bottom_text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Нижний текст раздела')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recomendation_blocks_b', to='api.Item', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.IntegerField(blank=True, null=True, verbose_name='Номер шага')),
                ('text', models.TextField(blank=True, max_length=255, null=True, verbose_name='Верхний текст раздела')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_steps', to='api.Item', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationSubBlockA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('amount', models.IntegerField(default=1, verbose_name='Количество')),
                ('block_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recomendation_sub_blocks_a', to='api.ItemRecomendationBlockA', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationSubBlockB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255, null=True, verbose_name='Текст')),
                ('row_number', models.IntegerField(default=1, verbose_name='Номер ряда')),
                ('block_b', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recomendation_sub_blocks_b', to='api.ItemRecomendationBlockB', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationSubBlockBImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='item/sub_block_b/images/', verbose_name='Изображение (xxx x xxx)')),
                ('block_b', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recomendation_sub_block_b_images', to='api.ItemRecomendationSubBlockB', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationSubBlockAItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Значение')),
                ('block_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recomendation_sub_block_a_items', to='api.ItemRecomendationSubBlockA', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationStepImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='item/step/images/', verbose_name='Изображение (xxx x xxx)')),
                ('step', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='step_images', to='api.ItemRecomendationStep', verbose_name='Относится к')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRecomendationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.ImageField(default=1, upload_to='', verbose_name='Порядок вывода')),
                ('image', models.ImageField(null=True, upload_to='item/recomendation/images/', verbose_name='Изображение (xxx x xxx)')),
                ('item_recomendation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_recomendation_images', to='api.ItemRecomendation', verbose_name='Относится к')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='difficulty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='difficulty', to='api.ItemDifficult', verbose_name='Сложность'),
        ),
        migrations.AddField(
            model_name='item',
            name='legend',
            field=models.ManyToManyField(blank=True, related_name='legends', to='api.ItemLegend', verbose_name='Условные обозначения'),
        ),
        migrations.AddField(
            model_name='item',
            name='material',
            field=models.ManyToManyField(blank=True, related_name='materials', to='api.ItemMaterial', verbose_name='Материалы'),
        ),
        migrations.CreateModel(
            name='CategoryTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название фильтра')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags', to='api.Category', verbose_name='Относится')),
            ],
        ),
    ]
