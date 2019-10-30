# Generated by Django 2.2.4 on 2019-10-30 06:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20191030_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.DecimalField(decimal_places='2', default=0, max_digits='9', validators=[django.core.validators.MaxValueValidator(100000000), django.core.validators.MinValueValidator(0)], verbose_name='Para'),
        ),
    ]