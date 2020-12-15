from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .forms import *

# Create your views here.
from employee.models import Students

def home(request):
    return render(request,'home.html')
def admin_login (request):
    context = {}
    if request.method == 'POST':
        user = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate (request , username = user , password = pwd)
        if user:
            return redirect ('/admindashboard')
        else:
            context['error'] = 'Provide Valid Credentials'
            return render (request,'auth/login.html',context)
    else:
        return render (request , 'auth/login.html')


def index (request):
    if request.method == 'POST':
        employee = EmployeeForm (request.POST , request.FILES)
        if employee.is_valid ():
            employee.save ()
            return redirect ('/index')
        else:
            return render (request , 'add_employee.html' ,
                           {'employees': employee})
    else:
        employee = EmployeeForm ()
        return render (request , 'add_employee.html' , {'employees': employee})


def addclass (request):
    if request.method == 'POST':
        classname = ClassForm (request.POST)
        if classname.is_valid ():
            classname.save ()
            return HttpResponse ('<h2>Class Added Successfully</h2>')
        else:
            return render (request , 'add_class.html' ,
                           {'classes': classname})
    else:
        classname = ClassForm ()
        return render (request , 'add_class.html' , {'classes': classname})
def edit_class(request,id):
    classes=AddClass.objects.get(id = id)
    return render(request,'edit_class.html',{'class':classes})
def update_class(request,id):
     classes=AddClass.objects.get(id=id)
     form= ClassForm(request.POST,instance = classes)
     if form.is_valid():
         form.save()
         return redirect('/totalclasses')
     return render(request,'edit_class.html',{'class':form})

def totalclasses (request):
    classes = AddClass.objects.all ()
    return render (request , 'view_class.html' , {'class_name': classes})


def delete_class (request , id):
    classes = AddClass.objects.get (id = id)
    classes.delete ()
    return redirect ('/totalclasses')


def viewemployees (request):
    employee = Employee.objects.all ()
    return render (request , 'view_employee.html' , {'employees': employee})


def delete_employee (request , id):
    employee = Employee.objects.get (id = id)
    employee.delete ()
    return redirect ('/viewemployees')


def admindashboard (request):
    student = Students.objects.all ().count ()
    employee = Employee.objects.all ().count ()
    context = {
        'students': student ,
        'employees': employee
    }
    return render (request , 'admin_dashboard.html' , context)
