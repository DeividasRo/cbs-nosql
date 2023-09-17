from connection import *


def add_screening(session_id, session_date, session_time, movie_title, auditorium):
    if r.exists(session_id):
        print()
        print(f"Session with ID {session_id} already exists.")
        return False
    if not r.sismember("auditoriums", auditorium):
        print()
        print(f"Auditorium '{auditorium}' does not exist.")
        return False

    screening_data = {
        'session_date': session_date,
        'session_time': session_time,
        'movie_title': movie_title,
        'auditorium': auditorium
    }

    r.hset(session_id, mapping=screening_data)


def get_screening(session_id):
    screening_data = r.hgetall(session_id)
    if screening_data:
        return {key.decode(): value.decode() for key, value in screening_data.items()}
    else:
        return None
