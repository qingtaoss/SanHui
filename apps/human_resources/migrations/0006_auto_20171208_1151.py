# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0005_auto_20171208_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'verbose_name': '户(家庭)信息', 'verbose_name_plural': '户(家庭)信息'},
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='degree_of_education',
            field=models.CharField(choices=[('cz', '初中及以下'), ('gz', '高中'), ('dz', '大专'), ('bk', '本科'), ('ss', '硕士'), ('bs', '博士')], default='cz', max_length=5, verbose_name='文化程度'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='political_status',
            field=models.CharField(choices=[('qz', '群众'), ('ty', '团员'), ('rdjjfz', '入党积极分子'), ('ybdy', '预备党员'), ('zsdy', '正式党员')], default='qz', max_length=6, verbose_name='政治面貌'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='working_salary',
            field=models.CharField(blank=True, choices=[('5', '5万以下'), ('5to8', '5-8万'), ('8to12', '8-12万'), ('12', '12万以上')], default='5', max_length=5, null=True, verbose_name='务工年收入'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='working_years',
            field=models.CharField(blank=True, choices=[('1', '1年以下'), ('1to5', '1-5年'), ('5', '5年以上')], default='1to5', max_length=4, null=True, verbose_name='务工年限'),
        ),
    ]
