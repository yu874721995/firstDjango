# Generated by Django 2.0.2 on 2018-07-31 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_auto_20180731_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_host',
            name='userid',
            field=models.IntegerField(max_length=10),
        ),
    ]