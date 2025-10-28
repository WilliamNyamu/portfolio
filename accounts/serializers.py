from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'password2', 'token']

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')

        if password is None or password2 is None:
            raise serializers.ValidationError('Password fields must be put')
        
        if password != password2:
            raise serializers.ValidationError('Both password fields should be the same')
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2') # remove password2

        # create user
        user = get_user_model().objects.create_user(**validated_data)
        # generate a token for the user.
        Token.objects.create(user=user)

        return user

    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'profile_picture', 'email', 'phone_number']