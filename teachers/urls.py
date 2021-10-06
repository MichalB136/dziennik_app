from django.urls import path
from .views import (
    TeacherClassDetalView, 
    TeacherPageView, 
    TeacherClassesListView)

urlpatterns = [
    path('teacherinfo/', TeacherPageView.as_view(), name='teacher_home'),
    path('teacher_classes/', TeacherClassesListView.as_view(), 
                                                name='teacher_classes'),
    path('teacher_classes/<int:pk>', TeacherClassDetalView.as_view(), 
                                                name='teacher_class_detail')
]

