from django import forms
from django.core.validators import MinValueValidator


class UserForm(forms.Form):
    user_id = forms.IntegerField(validators=[MinValueValidator(0)])
