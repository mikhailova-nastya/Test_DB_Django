# Generated by Django 3.2.9 on 2022-01-04 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220104_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell',
            old_name='disc',
            new_name='discount',
        ),
    ]
