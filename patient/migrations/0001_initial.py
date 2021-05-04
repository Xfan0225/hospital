# Generated by Django 3.1.3 on 2021-04-20 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientBase',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False, verbose_name='患者号')),
                ('pname', models.CharField(max_length=50, verbose_name='患者名字')),
                ('pgender', models.PositiveIntegerField(choices=[(1, '男'), (0, '女')], default=1, verbose_name='性别')),
                ('pbirth', models.DateField(verbose_name='出生日期')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
            ],
            options={
                'verbose_name': '患者基本信息',
                'verbose_name_plural': '患者基本信息',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('register_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='挂号id')),
                ('register_date', models.DateField(verbose_name='挂号日期')),
                ('status', models.PositiveIntegerField(choices=[(0, '未缴费'), (1, '缴费未看诊'), (2, '已经看诊')], default=0, verbose_name='当前状态')),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.department', verbose_name='科室号')),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctorbase', verbose_name='医生号')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientbase', verbose_name='病人号')),
            ],
            options={
                'verbose_name': '挂号信息',
                'verbose_name_plural': '挂号信息',
            },
        ),
    ]
