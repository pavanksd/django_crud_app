from employee_details.validation_form import EmployeeFieldValidation
from django.shortcuts import redirect, render
from .models import Employee
from django.contrib import messages
# Create your views here.
def index(request):
    employees = Employee.objects.all()
    return render(request,'index.html',{'employee':employees})

def createEmployee(request):
    context = {}
    if request.method == 'POST' :
        employee_form = EmployeeFieldValidation(request.POST)
        if employee_form.is_valid() :
            emp = Employee()
            emp.name = employee_form.cleaned_data['name']
            emp.email = employee_form.cleaned_data['email']
            emp.phone = employee_form.cleaned_data['phone']
            emp.save()
            return redirect('/')
        else:
            context['form_error'] = employee_form.errors.as_text()
            context['oldval'] = employee_form.cleaned_data
    return render(request,'create.html',context)

def editEmployee(request,id):
    context = {}
    emp  = Employee.objects.get(id = id )
    if request.method == 'POST' :
        employee_form = EmployeeFieldValidation(request.POST)
        if employee_form.is_valid() :
            emp.name = employee_form.cleaned_data['name']
            emp.email = employee_form.cleaned_data['email']
            emp.phone = employee_form.cleaned_data['phone']
            emp.save()
            messages.info(request,'Employee details updated')
            return redirect('/')
        else:
            context['form_error'] = employee_form.errors.as_text()

    context['employee_detail'] = emp
    return render(request,'update.html',context)

def deleteEmployee(request,id):
    emp  = Employee.objects.get(id = id )
    if(request.method == 'POST'):
        emp.delete()
        messages.info(request,'Employee deleted')
    return redirect('/')