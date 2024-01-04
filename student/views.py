from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Student_profile
from teacher.models import  Teacher_dashboard,Teacher_profile
from django.contrib.auth.decorators import login_required
import random
# Create your views here.
@login_required(login_url="login")
def course(request):
    return render(request,'course.html')



@login_required(login_url="login")
def feedback(request):
    return render(request,'feedback.html')


@login_required(login_url="login")
def About(request):
    return render(request,'about.html')

@login_required(login_url="login")
def anonymous_message(request):
    teacher_profile=Teacher_profile.objects.all()
    meeting_link=Teacher_dashboard.objects.all()

    paramerters={
        "teacher_profile":teacher_profile,
        "meeting_link":meeting_link
    }
    return render(request,'anonymous_message.html',paramerters)

@login_required(login_url="login")
def recorded_session(request):
    return render(request,'recorded_session.html')

@login_required(login_url="login")
def student_profile(request):
    user=request.user
    student_profile=Student_profile.objects.all()

    paramerters={
        "user":user,
        "student_profile":student_profile
    }
    return render(request,'student_profile.html',paramerters)



@login_required(login_url="login")
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')  
        cs = request.POST.get('cs')
        pn = request.POST.get('pn')
        el = request.POST.get('el')
        ad = request.POST.get('ad')
        pwd = request.POST.get('pwd')
        password_repeat = request.POST.get('password_repeat')

    if pwd == password_repeat:
        new_user = User.objects.create_user(
            username=username,
            email=el
        )
        new_user.set_password(pwd)
        new_user.save()

        new_profile = Student_profile.objects.create(
            first_name=fn,
            last_name=ln,
            course=cs,
            phone_number=pn,
            address=ad,
            email=el,
            user=new_user,
        )
        new_profile.save()
        return redirect('login')
    return render(request, 'login.html')
def login(request):
    if request.method == 'POST':
        username= request.POST.get('username')  
        pwd = request.POST.get('pwd')

        user = auth.authenticate(username=username, password=pwd)
        
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'login.html') 
def logout(request):
    auth.logout(request)
    return redirect("login")
