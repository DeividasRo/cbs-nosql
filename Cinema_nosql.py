import redis
import json
from datetime import datetime

r = redis.Redis(host='localhost', port=6379)

def add_screening(session_id, session_date, session_time, movie_title):
    screening_data = {
        'session_date': session_date,
        'session_time': session_time,
        'movie_title': movie_title
    }
    r.hset(session_id, mapping=screening_data)

def get_screening(session_id):
    screening_data = r.hgetall(session_id)
    if screening_data:
        return {key.decode(): value.decode() for key, value in screening_data.items()}
    else:
        return None

if __name__ == "__main__":
    sessions = [
        {"session_id": "session123", "session_date": "2023-09-18", "session_time": "15:00", "movie_title": "Movie Title 1"},
        {"session_id": "session456", "session_date": "2023-09-19", "session_time": "17:30", "movie_title": "Movie Title 2"}
    ]

    for session in sessions:
        add_screening(session['session_id'], session['session_date'], session['session_time'], session['movie_title'])

    for session in sessions:
        screening_details = get_screening(session['session_id'])
        if screening_details:
            print()
            for key, value in screening_details.items():
                print(f"{key}: {value}")
        else:
            print(f"No screening found for session {session['session_id']}.")
