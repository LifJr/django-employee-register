from cProfile import label
from django import forms
from django.forms import ModelForm
from django.db import models

# employee_register.models import Employee
from .models import Employee

class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        fields = ['fullname', 'emp_code', 'mobile', 'position']
        label = { 'fullname':'Full Name','emp_code':'Emp COde' }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"