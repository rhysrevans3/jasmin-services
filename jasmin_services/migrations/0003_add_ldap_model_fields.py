# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 15:39
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import jasmin_ldap_django.models


class Migration(migrations.Migration):

    dependencies = [
        ('jasmin_services', '0002_auto_20170112_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='ldapgroupbehaviour',
            name='group_name',
            field=models.CharField(default='NA', help_text='The name of the LDAP group to use.', max_length=100, verbose_name='LDAP group name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ldapgroupbehaviour',
            name='ldap_model',
            field=models.CharField(default='NA', help_text='The LDAP group model to use.', max_length=100, verbose_name='LDAP model'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='joinjiscmaillistbehaviour',
            name='joined_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]