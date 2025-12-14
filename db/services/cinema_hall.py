from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(
        cinemahall_name: CinemaHall,
        cinemahall_rows: CinemaHall,
        cinemahall_seat_in_row: CinemaHall) -> QuerySet:
    cinema_hall = CinemaHall.objects.filter(
        name=cinemahall_name,
        rows=cinemahall_rows,
        seat_in_row=cinemahall_seat_in_row
    )
    return cinema_hall
