from django.contrib import admin
from django.urls import path,include

from.import views
 

urlpatterns = [
   path('teacher/dashboard',views.dashboard,name='teacher/dashboard'),
   path('teacher/login',views.login,name='teacher/login'),
   path('teacher/anonymous_message',views.anonymous_message,name='teacher/anonymous_message'),
   path('teacher/recorded_session',views.recorded_session,name='teacher/recorded_session'),
   path('teacher/teacher_profile',views.teacher_profile,name='teacher/teacher_profile'),
]