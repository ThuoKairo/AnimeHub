from django.contrib import admin
from .models import Anime, UserAnimeList, Review

admin.site.register(Anime)
admin.site.register(UserAnimeList)
admin.site.register(Review)