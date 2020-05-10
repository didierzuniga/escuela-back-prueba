"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from users import views as viewUser
from courses import views as viewCourse
from modules import views as viewModule

urlpatterns = [
    path('signin/<str:username>/<str:password>', viewUser.signin),
    path('users/', viewUser.getAll),
    path('users/<int:id>', viewUser.get),
    path('courses/', viewCourse.getAll),
    path('courses/<int:id>', viewCourse.get),
    path('courses/get-info/<int:id>', viewCourse.getInfo),
    path('courses/student/<int:id>', viewCourse.getStudentCourses),
    path('courses/teacher/<int:id>', viewCourse.getTeacherCourses),
    path('modules/', viewModule.getAll),
    path('modules/<int:id>', viewModule.get),
    path('modules/student/<int:courseId>/<int:studentId>', viewModule.getStudentModules),
    path('modules/student/<int:courseLogId>', viewModule.getStudentModulesForTeacher),
    path('modules/student/update/<str:score>/<int:moduleLogId>', viewModule.updateStudentModule),
]
