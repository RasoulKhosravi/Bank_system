# Generated by Django 4.0.5 on 2022-06-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0011_remove_account_bank_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='operation',
            field=models.CharField(max_length=264),
        ),
    ]
