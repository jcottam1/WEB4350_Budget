# Generated by Django 4.2.6 on 2024-03-08 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0009_month_name_month_user_alter_budget_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default='2024-1-1'),
            preserve_default=False,
        ),
    ]
