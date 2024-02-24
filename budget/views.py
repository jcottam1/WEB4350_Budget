from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .forms import BudgetForm, MonthForm, BudgetCategoryForm, BudgetLabelForm, TransactionForm
from .models import Budget, BudgetCategory, BudgetLabel


# Create your views here.
def index(request):
    return render(request, 'budget/index.html')

@login_required(login_url='login')
def budget(request):
    categories = BudgetCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'budget/budget.html', context)

@login_required(login_url='login')
def make_budget(request):
    if request.method == "POST":
        form = BudgetForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('budget:budget')
    else:
        form = BudgetForm()
    return render(request, 'budget/form.html', {"form": form})

@login_required(login_url='login')
def category(request):
    return render(request, 'budget/category.html')

@login_required(login_url='login')
def make_category(request):
    if request.method == "POST":
        form = BudgetCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('budget:budget')
    else:
        form = BudgetCategoryForm()
    return render(request, 'budget/form.html', {"form": form})

def view_category(request, id):
    category = BudgetCategory.objects.get(id=id)
    labels = BudgetLabel.objects.all()
    context = {
        'category': category,
        'labels': labels
    }
    return render(request, 'budget/view_category.html', context)

@login_required(login_url='login')
def make_label(request):
    if request.method == "POST":
        form = BudgetLabelForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return redirect('budget:category')
    else:
        form = BudgetLabelForm()
    return render(request, 'budget/form.html', {"form": form})

@login_required(login_url='login')
def reports(request):
    return render(request, 'budget/reports.html')

@login_required(login_url='login')
def transactions(request):
    return render(request, 'budget/transactions.html')

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