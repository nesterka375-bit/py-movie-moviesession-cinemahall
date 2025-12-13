from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(
        moviesession_show_time: MovieSession,
        movie_id: MovieSession,
        cinemahall_id: MovieSession
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        movie_show_time=moviesession_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinemahall_id
    )
    return movie_session


def get_movies_sessions(session_date: MovieSession = None) -> QuerySet:
    movie_sessions = MovieSession.objects.all()
    if session_date is not None:
        movie_sessions = movie_sessions.filter(show_time__date=session_date)
    return movie_sessions


def get_movie_session_by_id(movie_session_id: MovieSession) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(
        moviesession_id: MovieSession,
        show_time: MovieSession = None,
        movie_id: MovieSession = None,
        cinema_hall_id: MovieSession = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=moviesession_id)
    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(movie_session_id: MovieSession) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    movie_session.delete()
    return movie_session
