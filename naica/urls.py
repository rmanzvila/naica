from django.urls import path
from naica.views import poll_list_view, poll_new_view


"""Specify allow URLS on project"""
urlpatterns = [
    path('', poll_list_view, name='polls'),
    path('new', poll_new_view, name='polls_new'),
]
