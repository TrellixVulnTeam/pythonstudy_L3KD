# Generated by Django 3.1.2 on 2020-10-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201022_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='useremail',
            field=models.EmailField(default='emailField', max_length=64, verbose_name='이메일'),
        ),
    ]
