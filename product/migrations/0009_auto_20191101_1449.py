# Generated by Django 2.2.4 on 2019-11-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20191030_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='hire_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Kiralama Tarihii'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='hire_end_date',
            field=models.DateTimeField(null=True, verbose_name='Kiralık Bitiş Tarihi'),
        ),
    ]
