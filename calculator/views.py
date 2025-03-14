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

    # clean session
    request.session.pop('solved_problems', None)

    context = {
        'form': form
    }

    return render(request, 'pages/home.html', context=context)


def calculate(request):

    # protect session
    if "first_field" not in request.session or "second_field" not in request.session or "operation" not in request.session:
        return redirect("homepage")

    # var_field passes how many digits there should be in in the number
    if request.method == 'POST':
        time = request.POST.get('time')

        if 'time' not in request.session:
            request.session['time'] = []

        request.session['time'].append(time)
        request.session.modified = True

    first_field = request.session.get('first_field', 1),
    second_field = request.session.get('second_field', 1),
    operation = request.session.get('operation', 'addition'),
    num_of_problems = request.session.get('num_of_problems', 1),

    solved_problems = request.session.get('solved_problems', 0)

    if solved_problems > num_of_problems[0] - 1:
        request.session['solved_problems'] = 0
        return redirect('summary')

    first_num_extrema = 10 ** (first_field[0] -
                               1), (10 ** first_field[0]) - 1
    second_num_extrema = 10 ** (second_field[0] -
                                1), (10 ** second_field[0]) - 1

    if operation[0] != 'division':
        first_num = random.randint(
            first_num_extrema[0], first_num_extrema[1])
        second_num = random.randint(
            second_num_extrema[0], second_num_extrema[1])

        if operation[0] == 'addition':
            res = first_num + second_num
        elif operation[0] == 'subtraction':
            res = first_num - second_num
        else:  # multiplication
            res = first_num * second_num

    else:
        while True:

            '''
            When dividing, we want to obtain integers and none of these 
            numbers can be longer than the number selected by the user.

            For this reason we need to take the following steps:
            1. the first number is the result of multiplying two numbers
            2. we check whether the result is not longer than what the 
            user selected (for the first number)
            '''

            quotient = random.randint(
                first_num_extrema[0], first_num_extrema[1])
            second_num = random.randint(
                second_num_extrema[0], second_num_extrema[1])

            first_num = second_num * quotient

            if first_num <= first_num_extrema[1]:
                break

        res = first_num / second_num

    solved_problems += 1
    request.session['solved_problems'] = solved_problems

    context = ({
        'first_num': first_num,
        'second_num': second_num,
        'operation': dict(Menu.math_operations)[operation[0]],
        'res': res,
        'num_of_problems': num_of_problems[0],
        'solved_problems': solved_problems,
        'nick': request.user.nickname if request.user.is_authenticated else "guest"
    })

    return render(request, 'pages/calculate.html', context)


def summary(request):

    # protect session
    if "first_field" not in request.session or "second_field" not in request.session or "operation" not in request.session:
        return redirect("homepage")
    
    if request.user.is_authenticated:
        request.user.number_of_sessions += 1
        request.user.save()

    times = [float(t) for t in request.session.get("time", [])]
    avg_time = round((sum(times) / len(times)), 2)

    # clean session
    request.session.pop('solved_problems', None)

    context = {
        'times': times,
        'avg_time': avg_time,
    }

    return render(request, 'pages/summary.html', context)


def abort(request):

    solved = len(request.session.get("time", []))
    if not solved:
        return redirect('homepage')

    return redirect('summary')

def set_layout_session(request):

    user = request.user
    
    return render(request, 'layouts/layout.html', {'user': user})
