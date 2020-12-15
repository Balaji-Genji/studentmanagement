from django.db import models


# Create your models here.
class Students (models.Model):
    name = models.CharField (max_length=100)
    address = models.TextField (max_length=100)
    class_name = models.CharField (max_length=50, default='class_name')
    mobile = models.IntegerField ()
    image = models.ImageField (upload_to='Students/')

    class Meta:
        db_table = 'students'


class Student_Attendance (models.Model):
    attendance_choices= {
                            'Present', 'Absent'
                        },
    student_id = models.IntegerField ()
    date = models.DateField ()
    am_or_pm = models.CharField (max_length=50)
    present_or_absent = models.CharField (max_length=50,choices=attendance_choices)


    class Meta:
        db_table = 'student_attendance'
