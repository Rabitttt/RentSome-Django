# Generated by Django 2.2.4 on 2019-11-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20191101_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='hire_start_date',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='hire_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]