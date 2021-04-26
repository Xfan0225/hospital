# Generated by Django 3.1.3 on 2021-04-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('med_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='药品id')),
                ('med_name', models.CharField(max_length=50, verbose_name='药品名称')),
                ('med_class', models.CharField(max_length=50, verbose_name='药品类别')),
                ('med_price', models.FloatField(verbose_name='药品价格')),
                ('med_stock', models.IntegerField(verbose_name='药品库存')),
                ('initial_py', models.CharField(max_length=50, verbose_name='药品快拼')),
            ],
            options={
                'verbose_name': '药品价格信息',
                'verbose_name_plural': '药品价格信息',
            },
        ),
    ]
