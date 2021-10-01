from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from students.models import Student

class HomePageView(TemplateView, LoginRequiredMixin):
    template_name = 'home.html'

class HomeRedirectView(RedirectView, LoginRequiredMixin):
    permament = False
    query_string = True
    pattern_name = ''

    def get_redirect_url(self, *args, **kwargs):
        logged_user = self.request.user
        if Student.objects.filter(user=logged_user):
            self.pattern_name = 'student_home'
        else:
            self.pattern_name = 'teacher_home'
        return super().get_redirect_url(*args, **kwargs)


class StudentPageView(TemplateView, LoginRequiredMixin):
    template_name = 'student_home.html'

class TeacherPageView(TemplateView, LoginRequiredMixin):
    template_name = 'student_home.html'