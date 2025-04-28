# employee/forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'salary', 'phone_number']

class EmployeeSearchForm(forms.Form):
    name = forms.CharField(required=False, label="Name")
    position = forms.CharField(required=False, label="Position")
    salary = forms.DecimalField(required=False, label="Salary", max_digits=10, decimal_places=2)