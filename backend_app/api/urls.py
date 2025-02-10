from django.urls import include, path
from .views import ContactsViewSet, ContactDetailView, TasksViewSet, TaskDetailView
from rest_framework import routers

urlpatterns = [
    path('contact/', ContactsViewSet.as_view()),
    path('contact/<int:pk>/',ContactDetailView.as_view(), name='contact-detail'),   
    path('task/', TasksViewSet.as_view()),
    path('task/<int:pk>/',TaskDetailView.as_view(), name='task-detail'),   
    
]

