from django.contrib import admin

# Register your models here.
from .models import Students,Student_Attendance
admin.site.register(Students)
admin.site.register(Student_Attendance)