from django.urls import path
from .views import HomePageView, HomeRedirectView 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('redirect-user/', HomeRedirectView.as_view(), name='home_redirect'),
]

