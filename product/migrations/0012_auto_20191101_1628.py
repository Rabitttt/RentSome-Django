# Generated by Django 2.2.4 on 2019-11-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20191101_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='hire_end_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Kiralık Bitiş Tarihi'),
        ),
    ]
