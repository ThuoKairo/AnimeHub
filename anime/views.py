from django.shortcuts import render, get_object_or_404, redirect
from .models import Anime, Review
from .forms import ReviewForm

def anime_list(request):
    animes = Anime.objects.all()
    return render(request, 'anime/anime_list.html', {'animes': animes})

def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    reviews = Review.objects.filter(anime=anime)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.anime = anime
            review.user = request.user
            review.save()
            return redirect('anime_detail', anime_id=anime.id)
    else:
        form = ReviewForm()
    return render(request, 'anime/anime_detail.html', {
        'anime': anime,
        'reviews': reviews,
        'form': form
    })