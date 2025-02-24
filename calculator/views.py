from django.shortcuts import render, redirect
from .forms import Menu
import random

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

    # var_field passes how many digits there should be in in the number
    first_field = request.session.get('first_field'),
    second_field = request.session.get('second_field'),
    operation = request.session.get('operation'),
    num_of_problems = request.session.get('num_of_problems'),

    first_num_extrema = 10 ** (first_field[0] - 1), (10 ** first_field[0]) - 1
    second_num_extrema = 10 ** (second_field[0] - 1), (10 ** second_field[0]) - 1

    first_num = random.randint(first_num_extrema[0], first_num_extrema[1])
    second_num = random.randint(second_num_extrema[0], second_num_extrema[1])

    return render(request, 'pages/calculate.html')
