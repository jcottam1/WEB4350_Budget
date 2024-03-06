from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .forms import BudgetForm, MonthForm, BudgetCategoryForm, BudgetLabelForm, TransactionForm
from .models import Budget, BudgetCategory, BudgetLabel, Transaction, Month
from django.db.models import Sum


# Create your views here.
def index(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions
    }
    return render(request, 'budget/index.html', context)

@login_required(login_url='login')
def budget(request):
    budgets = Budget.objects.all()
    categories = BudgetCategory.objects.all()
    months = Month.objects.all()
    context = {
        'budgets': budgets,
        'categories': categories,
        'months': months
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
    return render(request, 'budget/form.html', {"form": form})

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

    return render(request, 'budget/form.html', {"form": form, 'budget': budget})

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
    categories = BudgetCategory.objects.all()
    months = Month.objects.all()
    context = {
        'budget': budget,
        'categories': categories,
        'months': months,
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
    return render(request, 'budget/reports.html')

@login_required(login_url='login')
def transactions(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions
    }
    return render(request, 'budget/transactions.html', context)

@login_required(login_url='login')
def make_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('budget:transactions')
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
        return redirect('budget:transactions')
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

@login_required(login_url='login')
def make_month(request):
    if request.method == "POST":
        form = MonthForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('budget:budget')
    else:
        form = MonthForm()
    return render(request, 'budget/form.html', {"form": form})

