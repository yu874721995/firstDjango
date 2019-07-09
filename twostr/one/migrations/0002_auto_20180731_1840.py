# Generated by Django 2.0.2 on 2018-07-31 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_body',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=30)),
                ('value', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user_host',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.UserInfo'),
        ),
        migrations.AddField(
            model_name='user_body',
            name='host_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.user_host'),
        ),
    ]