# Generated by Django 2.2.1 on 2019-07-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0012_user_body_json_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_body',
            name='json_body',
        ),
        migrations.AddField(
            model_name='user_host',
            name='json_body',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user_host',
            name='json_header',
            field=models.CharField(default='', max_length=200),
        ),
    ]
