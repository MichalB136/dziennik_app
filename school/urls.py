from django.urls import path
from .views import StudentListView, StudentDetailView, StudentMarkView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('<uuid:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('<uuid:pk>/marks/', StudentMarkView.as_view(), name='student_marks'),
]

