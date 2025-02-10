from django.urls import path
from .views import UserProfileListView, UserProfileDetailView, SingUpView, LoginView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('profile/', UserProfileListView.as_view(), name='userprofile-list'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SingUpView.as_view(), name='signup'),
    
    
]