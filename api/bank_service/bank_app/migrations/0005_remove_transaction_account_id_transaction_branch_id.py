# Generated by Django 4.0.5 on 2022-06-21 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0004_transaction_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='account_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='branch_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bank_app.bankbranch'),
            preserve_default=False,
        ),
    ]
