from django.shortcuts import render
from .serializers import ContactSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Contact
from rest_framework import permissions




# Create your views here.

class ContactView(ListCreateAPIView):
    serializer_class= ContactSerializer
    permission_classes=(permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    


class DetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=ContactSerializer
    permission_classes=[permissions.IsAuthenticated]
    lookup_field='id'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

