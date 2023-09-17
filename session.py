from connection import *


def add_session(session_date, session_time, movie_title, auditorium):
    if not r.sismember("auditoriums", auditorium):
        print()
        print(f"\nAuditorium '{auditorium}' does not exist.")
        return

    session_data = {
        'session_date': session_date,
        'session_time': session_time,
        'movie_title': movie_title,
        'auditorium': auditorium
    }

    session_id = "session" + str(r.scard("sessions"))
    r.hset(session_id, mapping=session_data)
    r.sadd("sessions",  session_id)


def get_session(session_id):
    session_data = r.hgetall(session_id)
    if session_data:
        return {key.decode(): value.decode() for key, value in session_data.items()}
    else:
        return None


def get_reserved_seats(session_id):
    return set(map(lambda x: x.decode('utf-8'), r.smembers(f"{session_id}:reserved_seats")))
