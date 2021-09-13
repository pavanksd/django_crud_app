from django import forms

class EmployeeFieldValidation(forms.Form):
    name    = forms.CharField(max_length=100, error_messages={
               'required': 'Please enter your name'
                })
    email   = forms.EmailField()
    phone   = forms.CharField(max_length=10)