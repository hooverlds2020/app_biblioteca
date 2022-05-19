from django.shortcuts import render
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny

# Create your views here.
from .serializers import UserSerializer
from .models import User
#from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  User.objects.all()
    #permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
