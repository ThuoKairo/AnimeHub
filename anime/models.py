from django.db import models
from django.contrib.auth.models import User

class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class UserAnimeList(models.Model):
    CATEGORY_CHOICES = [
        ('watching', 'Watching'),
        ('on_hold', 'On Hold'),
        ('dropped', 'Dropped'),
        ('plan_to_watch', 'Plan to Watch'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.anime.title} ({self.category})"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    review_text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.anime.title} ({self.rating})"