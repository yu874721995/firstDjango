# Generated by Django 2.0.2 on 2018-08-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0006_auto_20180818_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_host',
            name='type',
            field=models.CharField(default='post', max_length=20),
        ),
    ]