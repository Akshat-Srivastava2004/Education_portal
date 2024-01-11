from django.shortcuts import render,redirect
from django.contrib import auth
from .models import Teacher_dashboard,Teacher_profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="teacher/login")
def dashboard(request):
    if request.method == 'POST':
        meetingLink=request.POST.get("meetingLink")
    
        teacher_profile= Teacher_dashboard.objects.create(
        link=meetingLink,

        )
        teacher_profile.save
        return redirect('teacher/dashboard')
    return render(request,'teacher/dashboard.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if Teacher_profile.objects.filter(username=username).exists():

         user= auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('teacher/dashboard')
        else:
            return redirect('teacher/login')
    return render(request,'teacher/login.html')

@login_required(login_url="teacher/login")
def anonymous_message(request):
    return render(request,'teacher/anonymous_message.html')

@login_required(login_url="teacher/login")
def recorded_session(request):
    return render(request,'teacher/recorded_session.html')


@login_required(login_url="teacher/login")
def teacher_profile(request):
    return render(request,'teacher/teacher_profile.html')

def teacher_logout(request):
    auth.logout(request)
    return redirect("teacher/login")