# Generated by Django 5.1.6 on 2025-03-05 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
