from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MONTH_CHOICES = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December')
)

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_name = models.CharField(max_length=100)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    new_month = models.CharField(choices=MONTH_CHOICES,blank=True, null=True, max_length=100)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.budget_name



class BudgetCategory(models.Model):
    category_name = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    planned = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    received = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.category_name

class BudgetLabel(models.Model):
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    planned = models.DecimalField(max_digits=10, decimal_places=2)
    received = models.DecimalField(max_digits=10, decimal_places=2, default=0)
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
    date = models.DateField()

    def __str__(self):
        return self.transaction_name
