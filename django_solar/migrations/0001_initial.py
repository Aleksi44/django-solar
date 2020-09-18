# Generated by Django 3.1.1 on 2020-09-17 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_send', models.BooleanField(default=False)),
                ('send_at', models.DateTimeField(default=datetime.datetime.now)),
                ('mail', models.EmailField(default=None, max_length=254, null=True)),
                ('subject', models.CharField(default='', max_length=100)),
                ('html', models.TextField(default=None)),
                ('text', models.TextField(default='')),
                ('from_mail', models.CharField(default='hello@snoweb.fr', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]