# Generated by Django 5.0.4 on 2024-05-02 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='items',
        ),
    ]
