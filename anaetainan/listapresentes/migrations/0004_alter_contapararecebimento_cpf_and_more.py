# Generated by Django 4.1.7 on 2024-04-18 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("listapresentes", "0003_contapararecebimento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contapararecebimento",
            name="cpf",
            field=models.CharField(
                blank=True, default="", max_length=32, verbose_name="CPF"
            ),
        ),
        migrations.AlterField(
            model_name="intencaodepresente",
            name="banco",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="listapresentes.contapararecebimento",
            ),
        ),
    ]
