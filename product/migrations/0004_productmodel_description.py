# Generated by Django 2.2.4 on 2019-10-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20191024_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama'),
        ),
    ]
