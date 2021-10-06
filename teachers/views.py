from django.contrib.auth import login
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    PermissionRequiredMixin
    )

from classes.models import SchoolClass, Mark, Subject

class TeacherPageView(
        LoginRequiredMixin, 
        PermissionRequiredMixin, 
        TemplateView):
    template_name = 'teacher_home.html'
    login_url = 'account_login'
    permission_required = 'teachers.is_teacher'


class TeacherClassesListView(
        LoginRequiredMixin, 
        PermissionRequiredMixin, 
        ListView):
    model = SchoolClass
    context_object_name = 'class_list'
    template_name = 'teachers/teacher_classes.html'
    login_url = 'account_login'
    permission_required = 'teachers.is_teacher'
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['teacher'] = Teacher.objects.all()
    #     return context

class TeacherClassDetalView(
        LoginRequiredMixin,
        PermissionRequiredMixin,
        DetailView
        ):
    model = SchoolClass
    context_object_name = 'class'
    template_name = 'teachers/teacher_detail_class.html'
    login_url = 'account_login'
    permission_required = 'teachers.is_teacher'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['mark'] = Mark.objects.all()
        context['subject'] = Subject.objects.all()
        return context 