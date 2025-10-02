from django.shortcuts import render, get_object_or_404
from django.db.models import  F, Sum, Max, Min, Count, Avg, Value
from .models import Movie
# Create your views here.


def show_all_movie(request):
    #movies = Movie.objects.order_by(F('year').asc(nulls_last=True))
    movies = Movie.objects.annotate(true_bool = Value(True),
                                    false_bool = Value(False),
                                    str_field = Value('Hello'),
                                    new_budget = F('budget') + 100,
                                    rating_year = F('rating') + F('year')
                                    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movie.html', {
        'movies': movies,
         'agg': agg})

def show_one_movie(request, slug):
    movie = get_object_or_404(Movie, slug = slug)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie})