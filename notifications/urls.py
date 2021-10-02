from django.urls import path

from .views import NotificationView, NotificationDetail

urlpatterns = [
    path('', NotificationView.as_view(), name='notifications-view'),
    path('<int:pk>/', NotificationDetail.as_view(), name='notifications-detail'),
]
