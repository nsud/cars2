# Generated by Django 2.2.10 on 2020-09-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200923_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True, default=1970, null=True),
        ),
    ]