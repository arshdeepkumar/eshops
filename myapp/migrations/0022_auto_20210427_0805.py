# Generated by Django 3.1.7 on 2021-04-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20210427_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=' ', max_length=122),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=' ', max_length=122),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default=' ', max_length=122),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=' ', max_length=122),
        ),
    ]
