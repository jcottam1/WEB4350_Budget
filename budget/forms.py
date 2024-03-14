from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Select, CheckboxInput
from budget.models import Budget, Month, BudgetCategory, BudgetLabel, Transaction


class DateInput(forms.DateInput):
    input_type = 'date'

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget

        fields = ['budget_name','total_budget', 'month']

        labels = {
            'budget_name': 'Budget Name',
            'total_budget': 'Total Budget',
            'month': 'Month',
        }

        widgets = {
            'budget_name': TextInput(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            }),
            'total_budget': NumberInput(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            }),
            'month': Select(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            })
        }

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

        labels = {
            'month': 'Month',
            'name': 'Name',
        }

        widgets = {
            'month': DateInput(attrs={
                'class': "form-control w-100 shadow border-0"
            }),
            'name': TextInput(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            })
        }

class BudgetCategoryForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ['category_name']

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
        fields = ['transaction_name', 'label','amount', 'incoming', 'outgoing', 'date']

        labels = {
            'transaction_name': 'Transaction Name',
            'label': 'Label',
            'amount': 'Amount',
            'incoming': 'Incoming',
            'outgoing': 'Outgoing',
            'date': 'Date ',
        }

        widgets = {
            'transaction_name': TextInput(attrs={
                'class': "form-control w-100 form-group shadow border-0",
                'placeholder': ''
            }),
            'label': TextInput(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            }),
            'amount': NumberInput(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            }),
            'incoming': CheckboxInput(attrs={
                'class': "h-100"
            }),
            'outgoing': CheckboxInput(attrs={
                'class': "form-control bg-warning shadow border-0",
                'placeholder': ''
            }),
            'date': DateInput(attrs={
                'class': "form-control w-100 shadow border-0"
            })
        }

