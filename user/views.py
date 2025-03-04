from django.shortcuts import render, redirect
from .forms import CustomUserForm, LoginForm
from django.contrib.auth import login, authenticate

# Create your views here.

def register(request):

    if request.method == "POST":
        
        form = CustomUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('panel')
    
    form = CustomUserForm()

    context = {
        'form': form
    }

    return render(request, 'pages/user_register.html', context)

def user_login(request):

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('panel')

    form = LoginForm()

    context = {'form': form}

    return render(request, 'pages/user_login.html', context)

def panel(request):

    return render(request, 'pages/user_panel.html')