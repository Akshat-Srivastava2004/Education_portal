from django.contrib import admin
from django.urls import path

from.import views
 

urlpatterns = [
    path('course',views.course,name='course'),
    path('recorded_session',views.recorded_session,name='recorded_session'),
    path('feedback',views.feedback,name='feedback'),
    path('student_profile',views.student_profile,name='student_profile'),
    path('About',views.About,name='About'),
    path('anonymous_message',views.anonymous_message,name='anonymous_message'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('assigment_submisson',views.assigment_submisson,name='assigment_submisson'),
]
