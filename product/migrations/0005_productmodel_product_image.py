# Generated by Django 2.2.4 on 2019-10-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_productmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ürün Resmi Ekleyin'),
        ),
    ]