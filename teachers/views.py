from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    PermissionRequiredMixin
    )


from classes.models import SchoolClass, Mark, Subject
from .forms import MarkCreateForm


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
        FormMixin,
        DetailView
        ):
    model = SchoolClass
    context_object_name = 'class'
    template_name = 'teachers/teacher_detail_class.html'
    login_url = 'account_login'
    permission_required = 'teachers.is_teacher'
    form_class = MarkCreateForm

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['mark'] = Mark.objects.filter(student__in=self.object.students.all())
        context['mark'] = Mark.objects.order_by('date')
        context['subject'] = Subject.objects.filter(teachers=self.request.user.teacher)
        return context 
    
    def get_success_url(self):
        return reverse('teacher_class_detail', kwargs={'pk' : self.object.id})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teacher
        form.save()
        return super(TeacherClassDetalView, self).form_valid(form)