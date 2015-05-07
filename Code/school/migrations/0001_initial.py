# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('englishName', models.CharField(max_length=64, null=True, blank=True)),
                ('number', models.CharField(unique=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('englishName', models.CharField(max_length=64, null=True, blank=True)),
                ('number', models.CharField(unique=True, max_length=128)),
                ('department', models.ForeignKey(to='school.Department')),
            ],
            options={
                'verbose_name': 'Major',
                'verbose_name_plural': 'Majors',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('englishName', models.CharField(max_length=64, null=True, blank=True)),
                ('number', models.CharField(unique=True, max_length=128)),
                ('campus', models.CharField(blank=True, max_length=16, null=True, choices=[(b'east', '\u4e1c\u6821\u533a'), (b'north', '\u5317\u6821\u533a'), (b'south', '\u5357\u6821\u533a'), (b'zhuhai', '\u73e0\u6d77\u6821\u533a')])),
                ('dean', models.CharField(max_length=16, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.AddField(
            model_name='major',
            name='school',
            field=models.ForeignKey(to='school.School'),
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(to='school.School'),
        ),
    ]
