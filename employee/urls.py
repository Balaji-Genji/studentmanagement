from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings

urlpatterns=[
 path ('admin/', admin.site.urls),
 path('student',views.student,name='Add Student'),
 #path('autocomplete',views.autocomplete,name='autocomplete'),
 path('viewstudents',views.view_students,name='view students'),
 path('delete_student/<int:id>',views.delete_student),
 path('studentattendance',views.studentattendance,name='Student Attendance'),
 path('employeedashboard',views.edashboard,name='Employee Dashboard'),
 path('addattendance',views.attendance_view,name='Add attendance'),
 path('search',views.search,name='Search Class Students'),
 path('employee_login',views.employee_login,name='Employee login'),
 path('totalattendance',views.totalattendance,name='View Attendance List')
 ]
if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
