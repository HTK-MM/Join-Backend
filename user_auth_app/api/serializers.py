from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name', 'last_name']
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile 
        fields = ['user', 'emblem', 'color']

class EmailAuthTokenSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)
  
  def validate(self, attrs):
            email = attrs.get('email')
            password = attrs.get('password')
        # Verifica si el usuario existe y es válido
            user = User.objects.filter(email=email).first()
            authenticated_user = authenticate(username=user.username, password=password)
            if not authenticated_user:
                    raise serializers.ValidationError('Invalid email or password')
            attrs['user'] = authenticated_user
            return attrs


class SingUpSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    emblem = serializers.CharField(write_only=True) 
    color = serializers.CharField(write_only=True)  
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password','repeated_password','first_name','last_name', 'emblem', 'color']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self): 
            pw = self.validated_data['password']
            repeated_pw = self.validated_data['repeated_password']
            if pw != repeated_pw:
               raise serializers.ValidationError({'password': 'Password must match'})
            user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
            )
            user.set_password(pw)
            user.save()
            
            emblem = self.validated_data['emblem']
            color = self.validated_data['color']
            UserProfile.objects.create(user=user, emblem=emblem, color=color)
            return user
    
