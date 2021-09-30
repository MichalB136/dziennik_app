from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class StudentPageView(TemplateView):
    template_name = 'student_home.html'