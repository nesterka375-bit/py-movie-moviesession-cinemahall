from xmlrpc.client import DateTime
from db.models import MovieSession


def create_movie_session(
        show_time: DateTime,
        movie_id: int,
        cinemahall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=show_time,
        id=movie_id,
        hall_id=cinemahall_id
    )
    return movie_session


def get_movies_sessions(session_date: DateTime = None) -> MovieSession:
    movie_sessions = MovieSession.objects.all()
    if session_date is not None:
        movie_sessions = movie_sessions.get(show_time__date=session_date)
    return movie_sessions


def get_movie_session_by_id(session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    return movie_session


def update_movie_session(
        session_id: int,
        show_time: DateTime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        movie_session.show_time = show_time
    if movie_id is not None:
        movie_session.movie_id = movie_id
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()
    return movie_session
