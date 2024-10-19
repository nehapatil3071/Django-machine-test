from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Client ViewSet
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)


# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated] 
    
    def get_queryset(self):
        client_id = self.kwargs.get('client_id')
        if client_id:
            # Return projects filtered by the specific client
            return Project.objects.filter(client_id=client_id)
        # If no client_id is provided, return all projects
        return Project.objects.all()
    
    def perform_create(self, serializer):
        # Automatically set the created_by field to the authenticated user
        serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        client_id = self.kwargs.get('client_id')  # Extract client_id from URL
        client = get_object_or_404(Client, id=client_id) 
        
        # Add client to the request data
        data = request.data.copy()
        data['client'] = client.id
        
        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
