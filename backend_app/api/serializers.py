from rest_framework import serializers
from backend_app.models import Tasks, Contacts
from django.contrib.auth.models import User

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset= User.objects.all()
    )

    class Meta:
        model = Tasks
        fields = '__all__'
        extra_kwargs = {
            'subtask': {'required': False}  
        }
        
#Este esta mal definido OJO, porque el user lo llamo dos veces de manera diferente, una como PrimaryKeyRelatedField y luego lo redifino como get_user
"""class TasksSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=Users.objects.all())
    def get_users(self, obj):
        return [user.name for user in obj.users.all()]
    class Meta:
        model = Tasks
        fields = '__all__' """
#Con este regreso mas detalles del user en lugar de solo el id, pero no se debe usar el get_user y el PrimaryKeyRelatedField:      
""" class TasksSerializer(serializers.ModelSerializer):
    users = UsersSerializer(many=True)  # Usa el serializer de Users para detalles

    class Meta:
        model = Tasks
        fields = '__all__' """