# Generated by Django 4.2.2 on 2023-07-27 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0003_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]