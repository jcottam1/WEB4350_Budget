from django import forms
from django.contrib import admin
from django.forms import ModelForm, TextInput, NumberInput, Select, CheckboxInput
from budget.models import Budget, BudgetCategory, BudgetLabel, Transaction


class DateInput(forms.DateInput):
    input_type = 'date'

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget

        fields = ['budget_name', 'total_budget', 'new_month', 'year']

        labels = {
            'budget_name': 'Budget Name',
            'total_budget': 'Total Budget',
            'new_month': 'Month',
            'year': 'Year'
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
            'new_month': Select(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            }),
            'year': NumberInput(attrs={
                'class': 'form-control w-100 shadow border',
                'placeholder': ''
            })
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        print("User:", user)
        super().__init__(*args, **kwargs)



class BudgetCategoryForm(forms.ModelForm):
    class Meta:
        model = BudgetCategory
        fields = ['category_name']

class BudgetLabelForm(forms.ModelForm):
    class Meta:
        model = BudgetLabel
        fields = ['label', 'planned', 'due_date', 'notes']
        widgets = {
            'due_date': DateInput()
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_name', 'label', 'amount', 'incoming', 'outgoing', 'date']

        labels = {
            'transaction_name': 'Transaction Name',
            'label': 'Category Type',
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
            'label': Select(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            }),
            'amount': NumberInput(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': '$0.00'
            }),
            'incoming': CheckboxInput(attrs={
                'class': "h-100"
            }),
            'outgoing': CheckboxInput(attrs={
                'class': "form-control bg-warning shadow border-0",
                'placeholder': ''
            }),
            'date': DateInput(attrs={
                'class': "form-control w-100 shadow border-0",
            })
        }

