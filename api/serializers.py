from .models import *
from rest_framework import serializers
import requests
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'password', 'email', 'first_name', 'last_name','avatar','role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def validate_id_user(self, value):
        try:
            response = requests.get(f"{settings.USERS_API_URL}/{value}/")
            if response.status_code != 200:
                raise serializers.ValidationError("User does not exist")
        except requests.exceptions.RequestException:
            raise serializers.ValidationError("could not connect to user api")
        return value    

    def validate_id_game(self, value):
        try:
            response = requests.get(f"{settings.GAMES_API_URL}/{value}")
            if response.status_code != 200:
                raise serializers.ValidationError("Game does not exist")
        except requests.exceptions.RequestException:
            raise serializers.ValidationError("could not connect to game api")
        return value
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate_id_user(self, value):
        try:
            response = requests.get(f"{settings.USERS_API_URL}/{value}/")  # Asegúrate que esta URL esté bien
            if response.status_code != 200:
                raise serializers.ValidationError("User does not exist")
        except requests.exceptions.RequestException:
            raise serializers.ValidationError("Could not connect to user API")
        return value
    
    def validate(self, attrs):
        target_type = attrs.get('target_type')
        target_id = attrs.get('target_id')

        if target_type == 'article':
            url = f"{settings.ARTICLES_API_URL}/{target_id}/"
        elif target_type == 'review':
            url = f"{settings.REVIEWS_API_URL}/{target_id}/"
        else:
            raise serializers.ValidationError("Invalid target_type")

        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise serializers.ValidationError(f"{target_type.capitalize()} with ID {target_id} does not exist")
        except requests.exceptions.RequestException:
            raise serializers.ValidationError(f"Could not connect to {target_type} API")

        return attrs
    
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Game
        fields='__all__'

class GameGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGenre
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

    def validate_id_user(self, value):
        try:
            response = requests.get(f"{settings.USERS_API_URL}/{value}/")  # Asegúrate que esta URL esté bien
            if response.status_code != 200:
                raise serializers.ValidationError("User does not exist")
        except requests.exceptions.RequestException:
            raise serializers.ValidationError("Could not connect to user API")
        return value
    
    def validate_id_game(self, value):
        try:
            response = requests.get(f"{settings.GAMES_API_URL}/{value}/")
            if response.status_code != 200:
                raise serializers.ValidationError("Game does not exist")
        except requests.exceptions.RequestException:
            raise serializers.ValidationError("could not connect to game api")
        return value