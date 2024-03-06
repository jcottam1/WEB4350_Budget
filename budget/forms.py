from django import forms
from budget.models import Budget, Month, BudgetCategory, BudgetLabel, Transaction


class DateInput(forms.DateInput):
    input_type = 'date'

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['budget_name','total_budget', 'month']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        print("User:", user)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['month'].queryset = Month.objects.filter(user=user)

class MonthForm(forms.ModelForm):
    class Meta:
        model = Month
        fields = ['month', 'name']
        widgets = {
            'month': DateInput()
        }

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

