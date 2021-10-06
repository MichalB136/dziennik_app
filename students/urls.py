from django.urls import path
from .views import StudentMarkView, StudentPageView

urlpatterns = [
    path('studentinfo/', StudentPageView.as_view(), name='student_home'),
    path('studentinfo/<uuid:pk>', StudentMarkView.as_view(),
                                                name='student_mark'),
]
