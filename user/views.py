from django.shortcuts import render
from .forms import CustomUserForm

# Create your views here.

def register(request):

    if request.method == "POST":
        
        form = CustomUserForm(request.POST)

        if form.is_valid():
            pass
    
    form = CustomUserForm()

    context = {
        'form': form
    }

    return render(request, 'pages/user_register.html', context)