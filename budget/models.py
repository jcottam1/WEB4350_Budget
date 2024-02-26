from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Month(models.Model):
    month = models.DateField()
    def __str__(self):
        return f"Month: {self.month}"
class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_name = models.CharField(max_length=100)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)

    def __str__(self):
        return self.budget_name



class BudgetCategory(models.Model):
    category_name = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    planned = models.DecimalField(max_digits=10, decimal_places=2)
    received = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category_name

class BudgetLabel(models.Model):
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    planned = models.DecimalField(max_digits=10, decimal_places=2)
    received = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    notes = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.label

class Transaction(models.Model):
    label = models.ForeignKey(BudgetLabel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    incoming = models.BooleanField(default=False)
    outgoing = models.BooleanField(default=False)
    transaction_name = models.CharField(max_length=100)

    def __str__(self):
        return self.transaction_name