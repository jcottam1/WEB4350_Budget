# Generated by Django 4.2.6 on 2024-03-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0012_remove_budget_month_budget_new_month_budget_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetlabel',
            name='received',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]