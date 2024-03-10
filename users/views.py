from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('budget:index')
        else:
            messages.error(request, 'Logged in Fail')

    context = {
        'nbar': 'login'
    }

    return render(request, 'users/login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("admin"))
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Welcome {username}. You are now logged in.')
            return redirect('budget:index')
    else:
        form = RegistrationForm()

    context = {
        'nbar': 'register',
        'form': form
    }
    return render(request, 'users/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')
