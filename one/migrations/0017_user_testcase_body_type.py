# Generated by Django 2.2.1 on 2019-07-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0016_auto_20190723_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_testcase_body',
            name='type',
            field=models.CharField(default=1, max_length=10),
        ),
    ]
