# Generated by Django 3.1.3 on 2021-04-28 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_auto_20210428_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='dept_directcor',
            new_name='dept_director',
        ),
    ]
