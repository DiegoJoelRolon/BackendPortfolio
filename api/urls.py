from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'games', GameViewSet, basename='game')
router.register(r'game-genres', GameGenreViewSet, basename='gamegenre')
router.register(r'genres', GenreViewSet, basename='genre') 
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'articles', ArticleViewSet, basename='article')
urlpatterns = [
    path('', include(router.urls)),
]