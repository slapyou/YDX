# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-11 08:26
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_bannercourse_figthcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseProgess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progess', models.IntegerField(default=0, verbose_name='当前学习时间')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_finish', models.BooleanField(default=False, verbose_name='是否看完')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户id')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Video', verbose_name='视频id')),
            ],
            options={
                'verbose_name': '视频进度',
                'verbose_name_plural': '视频进度',
            },
        ),
    ]