# Generated by Django 4.0.2 on 2022-02-19 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []  # type: ignore[var-annotated]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "currency",
                    models.SmallIntegerField(
                        choices=[
                            ("RUB", 0),
                            ("UAH", 1),
                            ("USD", 2),
                            ("EUR", 3),
                        ],
                        null=True,
                    ),
                ),
                ("price", models.FloatField(null=True)),
                ("rcon_command", models.TextField(null=True)),
                ("require_nick", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="PaymentProcess",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(max_length=32, null=True)),
                ("timestamp", models.TimeField(auto_now_add=True)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lib.item",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.TimeField(auto_now_add=True)),
                (
                    "process",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lib.paymentprocess",
                    ),
                ),
            ],
        ),
    ]
