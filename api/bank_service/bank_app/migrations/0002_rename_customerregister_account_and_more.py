# Generated by Django 4.0.5 on 2022-06-21 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerRegister',
            new_name='Account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='bank_branch_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='bank_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bank_app.account'),
            preserve_default=False,
        ),
    ]
