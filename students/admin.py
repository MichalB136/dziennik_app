from django.contrib import admin

from .models import Student
from classes.models import Mark

class MarkInline(admin.TabularInline):
    model = Mark

class StudentAdmin(admin.ModelAdmin):
    inlines =[
        MarkInline,
    ]
    list_display = ("user","first_name", "last_name", "sex", "profile_pic")

admin.site.register(Student, StudentAdmin)
