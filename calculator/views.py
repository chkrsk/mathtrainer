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
    first_field = request.session.get('first_field', 1),
    second_field = request.session.get('second_field', 1),
    operation = request.session.get('operation', 'addition'),
    num_of_problems = request.session.get('num_of_problems', 10),

    first_num_extrema = 10 ** (first_field[0] - 1), (10 ** first_field[0]) - 1
    second_num_extrema = 10 ** (second_field[0] - 1), (10 ** second_field[0]) - 1

    if operation[0] != 'division':
        first_num = random.randint(first_num_extrema[0], first_num_extrema[1])
        second_num = random.randint(second_num_extrema[0], second_num_extrema[1])

        if operation[0] == 'addition':
            res = first_num + second_num
        elif operation[0] == 'subtraction':
            res = first_num - second_num
        else: # multiplication
            res = first_num * second_num

    else:
        while True:
            quotient  = random.randint(first_num_extrema[0], first_num_extrema[1])
            second_num = random.randint(second_num_extrema[0], second_num_extrema[1])

            first_num = second_num * quotient
            
            if first_num <= first_num_extrema[1]:
                break

        res = first_num / second_num

    context = {
        'first_num': first_num,
        'second_num': second_num,
        'num_of_problems': num_of_problems,
        'res': res
    }

    return render(request, 'pages/calculate.html', context)
