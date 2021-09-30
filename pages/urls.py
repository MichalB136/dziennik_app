from django.urls import path
from .views import HomePageView, StudentPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('StudentInfo', StudentPageView.as_view(), name='student_home'),
]

