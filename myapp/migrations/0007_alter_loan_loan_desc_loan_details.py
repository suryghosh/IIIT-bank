# Generated by Django 5.0.7 on 2024-10-12 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_alter_customer_password_loan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="loan_desc",
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name="loan_details",
            fields=[
                (
                    "loan_details_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("loan_count", models.IntegerField()),
                ("due_payments", models.IntegerField()),
                ("penalties", models.IntegerField()),
                (
                    "account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.accountnumber",
                    ),
                ),
            ],
        ),
    ]
