from django.shortcuts import render, redirect
from .forms import CustomUserForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.

def register(request):

    if request.user.is_authenticated:
        return redirect('panel')

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

    if request.user.is_authenticated:
        return redirect('panel')

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

@login_required(login_url='login')
def panel(request):

    user = request.user

    profile = CustomUser.objects.get(id=user.id)

    context = {
        'nickname': profile.nickname.capitalize(),
        'email': profile.email,
        'number_of_session': profile.number_of_sessions,
        'date_joined': profile.date_joined,
    }

    return render(request, 'pages/user_panel.html', context)

def user_logout(request):

    logout(request)

    return redirect('homepage')
