from django import forms
from django.forms import fields

from .models import *


class StudentForm (forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


class StudentAttendanceForm(forms.ModelForm):
    class Meta:
        model=Student_Attendance
        fields='__all__'
