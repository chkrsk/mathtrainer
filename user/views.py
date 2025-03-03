from django.shortcuts import render, redirect
from .forms import CustomUserForm

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

def login(request):

    return render(request, 'pages/user_login.html')

def panel(request):

    return render(request, 'pages/user_panel.html')