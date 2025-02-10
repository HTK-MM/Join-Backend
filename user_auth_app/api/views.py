from rest_framework import generics
from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer, SingUpSerializer, EmailAuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class UserProfileListView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
  
    
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LoginView(ObtainAuthToken):
    serializer_class = EmailAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data={}
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']    
            token, _ = Token.objects.get_or_create(user=user)
            data= {"token": token.key,
                   "id": user.id,
                   "first_name": user.first_name,
                   "last_name": user.last_name,
                   "email": user.email,
                   "message": "Login Successfully!"}
        else:
            data = serializer.errors
        return Response(data)

""" class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data={}      
    
        if serializer.is_valid():
         
            user = serializer.validated_data['user'] 
            token, created = Token.objects.get_or_create(user=user)
            data= {"token": token.key,
                   "id": user.id,
                   "first_name": user.first_name,
                   "last_name": user.last_name,
                   "email": user.email,
                   "message": "Login Successfully!"}
        else:
            data = serializer.errors
        return Response(data)  """

        
    
class SingUpView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SingUpSerializer(data=request.data)
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data= {"token": token.key,
                   "first_name": saved_account.first_name,
                   "last_name": saved_account.last_name,
                   "email": saved_account.email,
                   "username": saved_account.username,
                   "message": "Successfully registered!"}
        else:
            data = serializer.errors
        return Response(data)
    
