from django.contrib import admin
from .models import Student_profile
# Register your models here.
@admin.register( Student_profile)
class  Student_profileAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","address","phone_number","email","course")
