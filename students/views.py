from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
    )
    
from .models import Student
from classes.models import Mark, Subject



# Create your views here.
class StudentPageView(
        LoginRequiredMixin, 
        PermissionRequiredMixin, 
        TemplateView):
    template_name = 'student_home.html'
    login_url = 'account_login'
    permission_required = 'students.is_student'


class StudentMarkView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = 'student'
    template_name = "students/student_mark.html"
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mark'] = Mark.objects.all()
        context['subject'] = Subject.objects.all()
        return context
