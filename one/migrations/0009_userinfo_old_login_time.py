# Generated by Django 2.2.1 on 2019-07-09 20:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0008_userinfo_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='old_login_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]