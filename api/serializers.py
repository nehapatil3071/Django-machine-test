from rest_framework import serializers
from .models import Client
from .models import Project
from django.contrib.auth.models import User

class UserInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField( read_only=True)
    
    
class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')  
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']
        read_only_fields = ['created_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserInputSerializer(many=True)
        
    client_name = serializers.CharField(source='client.client_name', read_only=True)  
    created_by = serializers.ReadOnlyField(source='created_by.username') 
    
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_name', 'users', 'created_at', 'created_by']
        read_only_fields = [ 'client_name', 'created_by']

    def create(self, validated_data):
        user_data = validated_data.pop('users',[])  
        user_ids = [user['id'] for user in user_data]  
        
        users = User.objects.filter(id__in=user_ids)
 
        # Extract the user IDs
        users = User.objects.filter(id__in=user_ids)  

        project = Project.objects.create(**validated_data)  
        project.users.set(users)  # Assign the users to the project
        project.save()
        return project

    def update(self, instance, validated_data):
        user_data = validated_data.pop('users', None)
        if user_data is not None:
            user_ids = [user['id'] for user in user_data if 'id' in user]  # Extract user IDs
            users = User.objects.filter(id__in=user_ids) 
            instance.users.set(users)  # Update users

        return super().update(instance, validated_data)