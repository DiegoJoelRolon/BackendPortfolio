from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.URLField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=[
        ('admin','Admin'),
        ('user','User'),
        ('moder','Moder')
    ])
    class Meta:
        db_table = 'user'
    def __str__(self):
        return self.username
    
class Comment(models.Model):
    id_comment = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    target_type = models.CharField(max_length=20, choices=[
        ('article', 'Article'),
        ('review', 'Review')
    ])
    target_id = models.IntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id_comment} content: {self.content[:30]}..."
    
class Game(models.Model):
    id_game = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    developer = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'game'
    def __str__(self):
        return self.title

class Genre(models.Model):
    id_genre = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)

    class Meta:
        db_table = 'genre'
    def __str__(self):
        return self.name    
    
class GameGenre(models.Model):
    id_gamegenre = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = 'gamegenre'
        unique_together = ('game', 'genre')

    def __str__(self):
        return self

class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return self.title    



class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'
    def __str__(self):
        return self.title              