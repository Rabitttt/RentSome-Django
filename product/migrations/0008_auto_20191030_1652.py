# Generated by Django 2.2.4 on 2019-10-30 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0007_rental'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='hirer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
    ]