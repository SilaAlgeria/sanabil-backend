# Generated by Django 2.0.9 on 2019-10-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0013_auto_20191028_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='besoin',
            name='délivré_par',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
