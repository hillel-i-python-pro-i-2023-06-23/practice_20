# Generated by Django 4.2.5 on 2023-09-09 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0004_remove_transaction_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]