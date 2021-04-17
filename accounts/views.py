from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

# register api view
class RegisterView(generics.CreateAPIView):
    # get queryset
    queryset = User.objects.all()
    # get queryset
    permission_classes = (AllowAny,)
    # get queryset
    serializer_class = RegisterSerializer


# Api for register
class RegisterView(generics.CreateAPIView):
    # get queryset
    queryset = User.objects.all()
    # permission_Classes
    permission_classes = (AllowAny,)
    # serializers
    serializer_class = RegisterSerializer


# Api for put patch delete User EndPoints for Users
class UserApiView(ModelViewSet):
    # get queryset
    queryset = User.objects.all()
    # permission_Classes
    permission_classes = [IsAuthenticated]
    # serializers
    serializer_class = UserSerializer
