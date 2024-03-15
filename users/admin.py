from django.contrib import admin
from budget.models import Budget,BudgetCategory, BudgetLabel, Transaction

# Register your models here.
admin.site.register(Budget)
admin.site.register(BudgetCategory)
admin.site.register(BudgetLabel)
admin.site.register(Transaction)
