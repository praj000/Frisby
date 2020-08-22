# Generated by Django 3.0.7 on 2020-08-22 20:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('New', '0017_auto_20200812_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 1, 46, 31, 557195), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 1, 46, 31, 558192), verbose_name='Date'),
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('img', models.ImageField(default='default.jpg', upload_to='')),
                ('name', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]