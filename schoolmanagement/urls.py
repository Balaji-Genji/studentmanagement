"""schoolmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
from schooladmin import views as v1

from django.conf import settings

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('index', v1.index, name='School Admin home page'),
    path ('add_class', v1.addclass, name='new class'),
    path('viewemployees',v1.viewemployees,name='Show Employee Details'),
    path ('', include ('employee.urls')),
    path('delete_employee/<int:id>',v1.delete_employee,name='Delete Employee Data'),
    path('totalclasses',v1.totalclasses,name='Show Classes'),
    path('delete_class/<int:id>',v1.delete_class,name='Delete Class'),
    path('admindashboard',v1.admindashboard,name='Admin Dashboard'),
    path('admin_login',v1.admin_login,name='Admin Login'),

]
if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
