from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Student



class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'school/student_list.html'

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'school/student_info.html'
    login_url = 'account_login'
