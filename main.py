from auditorium import *
from screening import *


def main():
    print("Welcome to the Cinema Booking System!")
    sessions = [
        {"session_id": "session1", "session_date": "2023-09-18",
            "session_time": "15:00", "movie_title": "Movie Title 1", "auditorium": "a1"},
        {"session_id": "session2", "session_date": "2023-09-19",
            "session_time": "18:00", "movie_title": "Movie Title 2", "auditorium": "a0"},
    ]
    auditoriums = [
        {"row_count": 10, "seats_per_row": 20}
    ]

    for auditorium in auditoriums:
        add_auditorium(auditorium["row_count"], auditorium["seats_per_row"])

    for session in sessions:
        add_screening(session["session_id"], session["session_date"],
                      session["session_time"], session["movie_title"], session["auditorium"])

   # for session in sessions:
   #    screening_details = get_screening(session["session_id"])
   #    if screening_details:
   #        print()
   #        for key, value in screening_details.items():
   #            print(f"{key}: {value}")


if __name__ == "__main__":
    main()


# https://redis.io/docs/clients/python/
