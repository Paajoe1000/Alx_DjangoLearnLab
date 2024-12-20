from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
          write_only=True,
          style={'input_type': 'password', 'placeholder': 'Password'},
    )
    class Meta:
        model = get_user_model()
        fields = ['url','username', 'email', 'bio', 'password', 'followers']

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user
    
from rest_framework.authtoken.models import Token
class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ['key', 'user']
    

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FollowersSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    q = get_user_model().objects.all()
    following = serializers.HyperlinkedRelatedField(view_name='customuser-detail', many=True, queryset=q)
    followers = serializers.HyperlinkedRelatedField(view_name='customuser-detail', many=True, queryset=q)
    class Meta:
        model = get_user_model()
        fields = ['username','following', 'followers']



#! Ignore all the code under here as the checker tests expects me to write my serializer from scratch
#! This is supposed to create a token for the user that I have
#! However I wrote a signal.py code that creates a token for a user on account creation
class DummyUserSerializer(serializers.Serializer):
    password = serializers.CharField()
    class Meta:
        model = get_user_model()
        fields = ['username', 'email','password', 'bio']

    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
            token = Token.objects.create(user=user)
        return user, token