# Generated by Django 2.2.1 on 2019-08-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0018_case_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='case_report',
            name='type',
            field=models.CharField(default=1, max_length=10),
        ),
    ]
