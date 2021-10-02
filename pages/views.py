from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from students.models import Student
from classes.models import Mark, Subject

class HomePageView(TemplateView, LoginRequiredMixin):
    template_name = 'home.html'
    login_url = 'account_login'


class HomeRedirectView(RedirectView, LoginRequiredMixin):
    permament = False
    query_string = True
    pattern_name = ''
    login_url = 'account_login'

    def get_redirect_url(self, *args, **kwargs):
        logged_user = self.request.user
        if Student.objects.filter(user=logged_user):
            self.pattern_name = 'student_home'
        else:
            self.pattern_name = 'teacher_home'
        return super().get_redirect_url(*args, **kwargs)


class StudentPageView(TemplateView, LoginRequiredMixin):
    template_name = 'student_home.html'
    login_url = 'account_login'


class TeacherPageView(TemplateView, LoginRequiredMixin):
    template_name = 'student_home.html'
    login_url = 'account_login'


class StudentMarkView(DetailView, LoginRequiredMixin):
    model = Student
    login_url = 'account_login'
    context_object_name = 'student'
    template_name = "students/student_mark.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mark'] = Mark.objects.all()
        context['subject'] = Subject.objects.all()
        return context
