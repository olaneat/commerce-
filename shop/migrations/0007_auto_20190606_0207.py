# Generated by Django 2.2.1 on 2019-06-06 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190604_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_imgs'),
        ),
    ]