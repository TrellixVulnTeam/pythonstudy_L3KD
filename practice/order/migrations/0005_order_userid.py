# Generated by Django 3.1.2 on 2020-10-28 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20201028_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='userid',
            field=models.CharField(default='None', max_length=64, verbose_name='구매자아이디'),
        ),
    ]
