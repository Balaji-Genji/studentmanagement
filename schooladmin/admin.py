from django.contrib import admin
from .models import Employee,AddClass,Employee_Attendance
# Register your models here.
admin.site.register(Employee)
admin.site.register(Employee_Attendance)
admin.site.register(AddClass)