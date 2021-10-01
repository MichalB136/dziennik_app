from django.contrib import admin

from .models import Mark, SchoolClass, Subject


admin.site.register(Subject)
admin.site.register(SchoolClass)
admin.site.register(Mark)