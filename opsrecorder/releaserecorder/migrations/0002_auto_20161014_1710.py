# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releaserecorder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='releaseapplication',
            name='field_name',
        ),
        migrations.AddField(
            model_name='releaseapplication',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=200, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='releaseapplication',
            name='status',
            field=models.CharField(choices=[('draft', '草稿中'), ('submitted', '已提交')], default='draft', help_text='申请单状态', max_length=100, verbose_name='申请单状态'),
        ),
        migrations.AlterField(
            model_name='releaseapplication',
            name='application_description',
            field=models.CharField(blank=True, help_text='关于应用的描述', max_length=200, verbose_name='应用描述'),
        ),
        migrations.AlterField(
            model_name='releaseapplication',
            name='deploy_note',
            field=models.TextField(help_text='此次发布的步骤说明', verbose_name='发布说明'),
        ),
        migrations.AlterField(
            model_name='releaseapplication',
            name='instance_count',
            field=models.IntegerField(default=2, help_text='申请应用部署的实例数量', verbose_name='应用部署的实例数'),
        ),
        migrations.AlterField(
            model_name='releaseapplication',
            name='os_type',
            field=models.CharField(choices=[('windows', 'Windows Server'), ('linux', 'Linux 64')], default='linux', help_text='应用部署的操作系统', max_length=100, verbose_name='操作系统'),
        ),
        migrations.AlterField(
            model_name='releaseapplication',
            name='responsible_username',
            field=models.CharField(blank=True, help_text='应用的负责人', max_length=200, verbose_name='负责人名称'),
        ),
    ]
