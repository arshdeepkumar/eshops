# Generated by Django 3.1.7 on 2021-04-27 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20210427_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
