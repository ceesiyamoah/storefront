# Generated by Django 5.1.6 on 2025-03-03 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_customer_options_remove_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can Cancel order')]},
        ),
    ]
