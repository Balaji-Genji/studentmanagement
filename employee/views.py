from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import JsonResponse , HttpResponse
from django.shortcuts import render , redirect
from .forms import *
from schooladmin.models import AddClass


# Create your views here.
def employee_login (request):
    context = {}
    if request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate (request , username=name , password=pwd)
        if user:
            return redirect ('/employeedashboard')
        else:
            context['error'] = 'Provide Valid Credentials'
            return render (request , 'auth/login.html' , context)
    else:
        return render(request,'auth/login.html')


def student (request):
    if request.method == 'POST':
        student = StudentForm (request.POST , request.FILES)
        if student.is_valid ():
            student.save ()
            return redirect ('/student')
        else:
            return render (request , 'add_student.html' , {'students': student})
    else:
        student = StudentForm ()
        student1 = AddClass.objects.all ()
        return render (request , 'add_student.html' , {'students': student , 'students1': student1})


def view_students (request):
    student = Students.objects.all ()
    return render (request , 'view_students.html' , {'students': student})


def delete_student (request , id):
    student = Students.objects.get (id=id)
    student.delete ()
    return redirect ('/viewstudents')


"""def autocomplete(request):
    if 'term' in request.GET:
        qs = Students.objects.filter (class_name_icontains=request.GET.get ('term'))
        class_names = list ()
        for class_name in qs:
            class_names.append (class_name.class_name)
        return JsonResponse (class_names, safe=False)
    return render (request, 'add_students_attendance.html')"""


def search (request):
    classes = AddClass.objects.all ()
    return render (request , 'search_class.html' , {'classnames': classes})


def studentattendance (request):
    if request.method == 'POST':
        attendance = StudentAttendanceForm (request.POST)
        if attendance.is_valid ():
            for stdatd in attendance:
                stdatd.pk=None
                stdatd.save ()

        else:
            studentids = Students.objects.all ()
            return render (request , 'add_students_attendance.html' ,
                           {'studentatd': attendance , 'studentids': studentids})
    else:
        studentids = Students.objects.all ()
        attendance = StudentAttendanceForm ()
        return render (request , 'add_students_attendance.html' , {'studentatd': attendance , 'studentids': studentids})


def edashboard (request):

    student=Students.objects.all().count()
    context = {
        'students':student,
    }
    return render (request , 'employee_dashboard.html',context)


def attendance_view (request):
    if request.method == 'POST':
        srch = request.POST['classname']
        if srch:
            attendance = Students.objects.filter (Q(class_name=srch))
            if attendance:
                return render (request , 'add_students_attendance.html' , {'attendances': attendance})
            else:
                return HttpResponse ('<h2>No records found</h2> <a href="/search">Back</a>')
        else:
            return HttpResponse ('<h2>No records found</h2> <a href="/search">Back</a>')
    else:
        return redirect ('/search')


def totalattendance(request):
    total=Student_Attendance.objects.all()
    return render(request,'view_attendance.html',{'totals':total})