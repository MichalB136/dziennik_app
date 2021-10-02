from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView


class NotificationView(ListView):
    template_name = 'notifications/notificaitons_list.html'
    context_object_name = 'notifications'



class NotificationDetail(DetailView):
    template_name = 'notifications/notificaitons_detail.html'
    context_object_name = 'notification'