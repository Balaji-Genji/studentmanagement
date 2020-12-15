from django.db import models


# Create your models here.
class Employee (models.Model):
    employee_name = models.CharField (max_length=100)
    designation = models.CharField (max_length=100)
    address = models.CharField (max_length=200)
    employee_image = models.ImageField (upload_to='Employees')
    mobile = models.IntegerField ()

    class Meta:
        db_table = 'employee'


class AddClass (models.Model):
    class_name = models.CharField (max_length=100)

    class Meta:
        db_table = 'class_details'


class Employee_Attendance (models.Model):
    employee_id = models.ForeignKey (Employee, on_delete=models.CASCADE)
    date = models.DateTimeField (auto_now=True)
    am_or_pm = models.CharField (max_length=10)
    present_or_absent = models.CharField (max_length=20)

    class Meta:
        db_table = 'employee_attendance'
