from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BudgetForm, BudgetCategoryForm, BudgetLabelForm, TransactionForm
from .models import Budget, BudgetCategory, BudgetLabel, Transaction
from django.db.models import Sum
from time import strftime
from django.utils import timezone


# Create your views here.
@login_required(login_url='login')
def index(request):
    transactions = Transaction.objects.all()
    budgets = Budget.objects.all()
    context = {
        'nbar': 'dashboard',
        'transactions': transactions,
        'budgets': budgets
    }
    return render(request, 'budget/index.html', context)

@login_required(login_url='login')
def dashboard(request, id):
    transactions = Transaction.objects.all()
    budget = Budget.objects.get(id=id)
    budgets = Budget.objects.all()
    current_year = strftime("%Y")
    current_month = strftime('%m')
    current_day = strftime('%d')
    if current_month == "01" or current_month == "03" or current_month == "05" or current_month == "07" or current_month == "08" or current_month == "10" or current_month == "12":
        days_left = 31 - int(current_day)
    elif current_month == "04" or current_month == "06" or current_month == "09" or current_month == "11":
        days_left = 30 - int(current_day)
    elif current_month == "02" and current_year % 4 == 0:
        if current_year % 100 == 0:
            if current_year % 400 == 0:
                days_left = 29 - int(current_day)
            else:
                days_left = 28 - int(current_day)
        else:
            days_left = 29 - int(current_day)
    else:
        days_left = 28 - int(current_day)

    spending_limit = budget.total_budget/days_left
    context = {
        'nbar': 'dashboard',
        'transactions': transactions,
        'budget': budget,
        'budgets': budgets,
        'current_month': current_month,
        'spending_limit': spending_limit,
        'current_day': current_day,
        'days_left': days_left
    }
    return render(request, 'budget/dashboard.html', context)

@login_required(login_url='login')
def budget(request):
    budgets = Budget.objects.all()
    categories = BudgetCategory.objects.all()
    context = {
        'nbar': 'budget',
        'budgets': budgets,
        'categories': categories,
    }
    return render(request, 'budget/budget.html', context)

@login_required(login_url='login')
def make_budget(request):
    if request.method == "POST":
        form = BudgetForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('budget:budget')
    else:
        form = BudgetForm(user=request.user)

    context = {
        'nbar': 'budget',
        'form_name': 'Create Budget',
        'form': form
    }

    return render(request, 'budget/form.html', context)

@login_required(login_url='login')
def edit_budget(request, id):
    budget = Budget.objects.get(id=id)
    form = BudgetForm(request.POST or None, instance=budget)
    if form.is_valid():
        f = form.save(commit=False)
        f.user = request.user
        f.save()
        return redirect('budget:view_budget', id)
    else:
        form = form

    context = {
        'nbar': 'budget',
        'form_name': 'View Budget',
        'form': form,
        'budget': budget
    }

    return render(request, 'budget/form.html', context)

@login_required(login_url='login')
def delete_budget(request, id):
    budget = Budget.objects.get(id=id)

    if request.method == "POST":
        budget.delete()
        return redirect('budget:budget')

    return render(request, 'budget/delete.html', {'budget': budget})

@login_required(login_url='login')
def view_budget(request, id):
    budget = Budget.objects.get(id=id)
    income_transactions = Transaction.objects.filter(incoming=True)
    budgets = Budget.objects.all()
    cateogries = BudgetCategory.objects.all()
    context = {
        'budget': budget,
        'income_transactions':income_transactions,
        'budgets': budgets,
        'categories': cateogries
    }
    return render(request, 'budget/view_budget.html', context)

@login_required(login_url='login')
def make_category(request, id):
    if request.method == "POST":
        form = BudgetCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.budget = Budget.objects.get(id=id)
            f.save()
            return redirect('budget:view_budget', id)
    else:
        form = BudgetCategoryForm()
    return render(request, 'budget/form.html', {"form": form})


@login_required
def edit_category(request, id):
    category = BudgetCategory.objects.get(id=id)
    form = BudgetCategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        return redirect('budget:view_category', id)
    else:
        form = form

    return render(request, 'budget/form.html', {"form": form, 'category': category})

@login_required(login_url='login')
def delete_category(request, id):
    category = BudgetCategory.objects.get(id=id)

    if request.method == "POST":
        category.delete()
        return redirect('budget:view_budget', category.budget.id)

    return render(request, 'budget/delete.html', {'category': category})

@login_required(login_url='login')
def view_category(request, id):
    category = BudgetCategory.objects.get(id=id)
    labels = BudgetLabel.objects.all()
    total_planned = BudgetLabel.objects.filter(category=category).aggregate(Sum('planned'))['planned__sum']
    total_received = BudgetLabel.objects.filter(category=category).aggregate(Sum('received'))['received__sum']
    context = {
        'category': category,
        'labels': labels,
        'total_planned': total_planned,
        'total_received': total_received

    }
    return render(request, 'budget/view_category.html', context)

@login_required(login_url='login')
def make_label(request, id):
    if request.method == "POST":
        form = BudgetLabelForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.category = BudgetCategory.objects.get(id=id)
            f.save()
            return redirect('budget:view_category', id)
    else:
        form = BudgetLabelForm()
    return render(request, 'budget/form.html', {"form": form})

@login_required(login_url='login')
def edit_label(request, id):
    label = BudgetLabel.objects.get(id=id)
    form = BudgetLabelForm(request.POST or None, instance=label)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        return redirect('budget:view_category', label.category.id)
    else:
        form = form

    return render(request, 'budget/form.html', {"form": form, 'label': label})

@login_required(login_url='login')
def delete_label(request, id):
    label = BudgetLabel.objects.get(id=id)

    if request.method == "POST":
        label.delete()
        return redirect('budget:view_category', label.category.id)

    return render(request, 'budget/delete.html', {'label': label})

@login_required(login_url='login')
def reports(request):
    context = {
        'nbar': 'reports',
    }
    return render(request, 'budget/reports.html', context)

@login_required(login_url='login')
def transactions(request):
    transactions = Transaction.objects.all()
    budgets = Budget.objects.all()
    context = {
        'nbar': 'transactions',
        'transactions': transactions,
        'budgets': budgets
    }
    return render(request, 'budget/transactions.html', context)

@login_required(login_url='login')
def make_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('budget:view_transactions', f.label.category.budget.id)
    else:
        form = TransactionForm()
    return render(request, 'budget/form.html', {"form": form})

@login_required(login_url='login')
def edit_transaction(request, id):
    transaction = Transaction.objects.get(id=id)
    form = TransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        f = form.save(commit=False)
        f.save()
        return redirect('budget:view_transactions', transaction.label.category.budget.id)
    else:
        form = form

    return render(request, 'budget/form.html', {"form": form, 'transaction': transaction})

@login_required(login_url='login')
def delete_transaction(request, id):
    transaction = Transaction.objects.get(id=id)

    if request.method == "POST":
        transaction.delete()
        return redirect('budget:transactions')

    return render(request, 'budget/delete.html', {'transaction': transaction})

def view_transactions(request, id):
    transactions = Transaction.objects.all()
    budget = Budget.objects.get(id=id)
    context = {
        'transactions': transactions,
        'budget': budget,
    }
    return render(request, 'budget/view_transactions.html', context)

