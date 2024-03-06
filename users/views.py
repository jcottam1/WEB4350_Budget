from django.shortcuts import render, redirect, reverse
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
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
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
