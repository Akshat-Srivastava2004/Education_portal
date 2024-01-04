from django.contrib import admin
from .models import Teacher_dashboard,Teacher_profile

# Register your models here.
@admin.register(Teacher_dashboard)
class  teacher_dashboardAdmin(admin.ModelAdmin):
    list_display=("link","timestamp")

@admin.register(Teacher_profile)
class  Teacher_profileAdmin(admin.ModelAdmin):
    list_display=("username","first_name","last_name","course","email","password")
