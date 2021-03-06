# Generated by Django 2.1.8 on 2019-09-02 11:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190830_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions_datail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='景点名称')),
                ('address', models.CharField(max_length=100, verbose_name='详细地址')),
                ('datail', ckeditor.fields.RichTextField(verbose_name='详情信息')),
                ('sugget', models.FloatField(verbose_name='是否推荐,1为推荐')),
                ('city', models.CharField(max_length=40, verbose_name='所在省')),
                ('area', models.CharField(max_length=40, verbose_name='所在市')),
                ('summary', models.CharField(max_length=100, verbose_name='概要')),
                ('type', models.CharField(max_length=50, verbose_name='景点类型')),
            ],
            options={
                'verbose_name': '景点信息',
                'verbose_name_plural': '景点详情信息',
                'db_table': 'Attractions',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='attractions_price',
            options={'managed': False, 'verbose_name': '景点门票价格', 'verbose_name_plural': '景点门票价格信息'},
        ),
        migrations.AlterModelOptions(
            name='banner_img',
            options={'managed': False, 'verbose_name': '轮播图', 'verbose_name_plural': '轮播图片信息'},
        ),
        migrations.AlterModelOptions(
            name='flow',
            options={'managed': False, 'verbose_name': '景点流量信息', 'verbose_name_plural': '景点流量详情信息'},
        ),
        migrations.AlterModelOptions(
            name='home_infor',
            options={'managed': False, 'verbose_name': '房间信息', 'verbose_name_plural': '房间详情信息'},
        ),
        migrations.AlterModelOptions(
            name='hotel_datail',
            options={'managed': False, 'verbose_name': '酒店详情', 'verbose_name_plural': '酒店详情信息'},
        ),
        migrations.AlterModelOptions(
            name='hotel_infor',
            options={'managed': False, 'verbose_name': '酒店房间信息', 'verbose_name_plural': '酒店房间信息'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'managed': False, 'verbose_name': '新闻', 'verbose_name_plural': '新闻详情信息'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'managed': False, 'verbose_name': '订单信息', 'verbose_name_plural': '订单详情信息'},
        ),
        migrations.AlterModelTable(
            name='hotel_datail',
            table='Hotel_datail',
        ),
    ]
