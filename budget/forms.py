from django import forms
from budget.models import Budget, Month, BudgetCategory, BudgetLabel, Transaction


class DateInput(forms.DateInput):
    input_type = 'date'

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
        fields = ['category_name', 'planned', 'received']

class BudgetLabelForm(forms.ModelForm):
    class Meta:
        model = BudgetLabel
        fields = ['label', 'planned', 'received', 'due_date', 'notes']
        widgets = {
            'due_date': DateInput()
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_name', 'label','amount', 'incoming', 'outgoing']