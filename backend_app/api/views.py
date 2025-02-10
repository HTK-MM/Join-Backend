
from .serializers import ContactsSerializer, TasksSerializer
from backend_app.models import Contacts, Tasks
from rest_framework import generics
from .permissions import IsAuthenticatedOrReadOnly


class ContactsViewSet(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]      


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]      


class TasksViewSet(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly]      

    
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]      


