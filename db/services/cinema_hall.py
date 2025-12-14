from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(
        cinemahall_name: str,
        cinemahall_rows: int,
        cinemahall_seat_in_row: int) -> CinemaHall:
    cinema_hall = CinemaHall.objects.create(
        name=cinemahall_name,
        rows=cinemahall_rows,
        seat_in_row=cinemahall_seat_in_row
    )
    return cinema_hall
