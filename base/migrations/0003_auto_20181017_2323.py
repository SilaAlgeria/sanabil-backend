# Generated by Django 2.0.5 on 2018-10-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20181017_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dontype',
            name='label',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
