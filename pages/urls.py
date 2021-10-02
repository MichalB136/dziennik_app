from django.urls import path
from .views import HomePageView, HomeRedirectView 
from .views import StudentMarkView, StudentPageView, TeacherPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('redirect-user/', HomeRedirectView.as_view(), name='home_redirect'),
    path('studentinfo/', StudentPageView.as_view(), name='student_home'),
    path('teacherinfo/', TeacherPageView.as_view(), name='teacher_home'),
    path('studentinfo/<uuid:pk>', StudentMarkView.as_view(), name='student_mark'),
]

