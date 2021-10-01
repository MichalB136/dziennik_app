from django.urls import path
from .views import HomePageView, HomeRedirectView, StudentPageView, TeacherPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('redirect-user', HomeRedirectView.as_view(), name='home_redirect'),
    path('StudentInfo', StudentPageView.as_view(), name='student_home'),
    path('TeacherInfo', TeacherPageView.as_view(), name='teacher_home'),
]

