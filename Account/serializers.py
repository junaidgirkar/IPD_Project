from django.contrib.auth import authenticate
from .models import User

from rest_framework import serializers

#User._meta.get_field('email')._unique = True




class UserRegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "email", "password", )










class UserSerializer(serializers.Serializer):
    id = serializers.CharField()

    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    #is_m = serializers.CharField(max_length=255, default="True")
    #password = serializers.PasswordField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)





class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            last_name =validated_data['last_name'],
            email =validated_data['email'],
            first_name =validated_data['first_name'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user





class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

""" --- NEW STUFF ---"""


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

# Register Serializer
class RegisterSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'],password= validated_data['password'], last_name= validated_data['last_name'],first_name= validated_data['first_name'])

        return user


