# Generated by Django 4.2.6 on 2024-04-01 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0016_remove_transaction_user_budgetlabel_user'),
    ]


