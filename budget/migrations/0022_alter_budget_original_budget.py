# Generated by Django 4.2.6 on 2024-04-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0021_budget_original_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='original_budget',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
