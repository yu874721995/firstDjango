# Generated by Django 2.2.1 on 2019-07-18 20:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0013_auto_20190717_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='casecp_mk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(default=1, max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('subjection', models.CharField(default='', max_length=20)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
