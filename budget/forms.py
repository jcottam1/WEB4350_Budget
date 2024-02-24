from django import forms
from budget.models import Budget, Month, BudgetCategory, BudgetLabel, Transaction

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['total_budget', 'month']

class MonthForm(forms.ModelForm):
    class Meta:
        model = Month
        fields = ['month']

class BudgetCategoryForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ['category_name']

class BudgetLabelForm(forms.ModelForm):
    class Meta:
        model = BudgetLabel
        fields = ['category','label', 'planned', 'received', 'due_date', 'notes']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']