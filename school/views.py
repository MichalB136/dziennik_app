from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Student, Subject, Mark



class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'school/student_list.html'

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'school/student_info.html'
    login_url = 'account_login'


class StudentMarkView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'school/student_mark.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marks'] = Mark.objects.all()
        return context