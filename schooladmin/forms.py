from django import forms
from .models import *


class EmployeeForm (forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class ClassForm (forms.ModelForm):
    class Meta:
        model = AddClass
        fields = '__all__'
