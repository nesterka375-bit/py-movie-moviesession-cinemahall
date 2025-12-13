from django.db.models import QuerySet
from db.models import Movie


def get_movies(
        genres_ids: Movie = None,
        actors_ids: Movie = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.all()
    if genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)

    if actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movies_by_id(movie_id: Movie) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: Movie,
        movie_description: Movie,
        genres_ids: Movie = None,
        actors_ids: Movie = None
) -> QuerySet[Movie]:
    queryset = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids is not None:
        queryset = Movie.genres.add(genre_id=genres_ids)
    if actors_ids is not None:
        queryset = Movie.actors.add(actor_id=actors_ids)
    return queryset
