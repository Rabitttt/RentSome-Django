# Generated by Django 2.2.4 on 2019-11-04 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20191104_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='hirer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
