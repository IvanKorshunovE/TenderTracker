# Generated by Django 4.2.5 on 2023-09-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tender",
            fields=[
                (
                    "tender_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, max_digits=20, null=True),
                ),
                ("date_modified", models.DateTimeField(null=True)),
            ],
            options={
                "ordering": ["-date_modified"],
            },
        ),
    ]
