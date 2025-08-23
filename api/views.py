from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [AllowAny]  
        else:
            permission_classes = [IsAuthenticated]  
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Retorna los datos del usuario autenticado"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ReviewSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameGenreViewSet(viewsets.ModelViewSet):
    queryset = GameGenre.objects.all()
    serializer_class = GameGenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    