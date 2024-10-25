# Generated by Django 5.0.7 on 2024-10-25 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_transaction_processing', '0008_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_id',
            new_name='duc_account_id',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='account_name',
            new_name='duc_account_name',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='account_type',
            new_name='duc_account_type',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='created_at',
            new_name='duc_created_at',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='updated_at',
            new_name='duc_updated_at',
        ),
        migrations.AlterModelTable(
            name='account',
            table='Dupay_accounts',
        ),
    ]
