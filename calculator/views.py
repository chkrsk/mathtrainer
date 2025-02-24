from django.shortcuts import render, redirect
from .forms import Menu

# Create your views here.

def homepage(request):

    if request.method == 'POST':
        form = Menu(request.POST)
        if form.is_valid():
            request.session['first_field'] = form.cleaned_data['first_field']
            request.session['second_field'] = form.cleaned_data['second_field']
            request.session['operation'] = form.cleaned_data['operation']
            request.session['num_of_problems'] = form.cleaned_data['num_of_problems']

            return redirect('calculate')
    
    else:
        form = Menu()

    context = {
        'form': form
    }

    return render(request, 'pages/home.html', context=context)

def calculate(request):

    context = {
        'first_field': request.session.get('first_field'),
        'second_field': request.session.get('second_field'),
        'operation': request.session.get('operation'),
        'num_of_problems': request.session.get('num_of_problems'),
    }

    return render(request, 'pages/calculate.html', context=context)