# Generated by Django 3.1 on 2020-08-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200823_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='tag',
            field=models.CharField(max_length=200, null=True, verbose_name='태그'),
        ),
    ]