# Generated by Django 4.0.5 on 2022-06-22 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0005_remove_transaction_account_id_transaction_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='atm_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bank_app.atm'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='branch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bank_app.bankbranch'),
        ),
    ]