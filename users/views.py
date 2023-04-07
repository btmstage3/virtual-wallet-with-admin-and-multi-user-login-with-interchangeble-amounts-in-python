from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

@login_required(login_url='/login/')
def home(request):
    print('Home view accessed.')
    return render(request, 'home.html')

def login_view(request):
    print('Login view accessed.')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user(), form.get_password())
            print('User authenticated.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html', {'form': form})

def redirect_to_login(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('home')
