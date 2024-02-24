from django.contrib import admin
from budget.models import Budget, Month, BudgetCategory, BudgetLabel, Transaction

# Register your models here.
admin.site.register(Budget)
admin.site.register(Month)
admin.site.register(BudgetCategory)
admin.site.register(BudgetLabel)
admin.site.register(Transaction)
