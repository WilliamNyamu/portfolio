from django.shortcuts import render
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes, api_view
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        raise ValueError("Both fields must be included!")
    
    user = authenticate(email=email, password=password) # automatically check the given user credentials
    if user:
        token = Token.objects.get(user=user)
        return Response (
            {
                'token': token.key,
                'user_id': user.id,
                'user_email': user.email,
                'message': 'Login successful :) '
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response (
            {
                'error': 'User not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )

