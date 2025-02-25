from django import forms


class Menu(forms.Form):

    math_operations = (
        ('addition', '+'),
        ('subtraction', '-'),
        ('multiplication', '*'),
        ('division', '/'),
    )

    first_field = forms.IntegerField(min_value=1, required=True)
    second_field = forms.IntegerField(min_value=1, required=True)
    operation = forms.ChoiceField(choices=math_operations, required=False)
    num_of_problems = forms.IntegerField(
        min_value=1, required=False, label="number of problems")
