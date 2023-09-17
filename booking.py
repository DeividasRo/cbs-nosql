from connection import *
from session import *
from auditorium import *
import time


def buy_ticket(session_id, seat_id):
    session = get_session(session_id)
    if session is None:
        print("\nThis session does not exist.")
        return

    auditorium = get_auditorium(session["auditorium"])

    if (int(seat_id) < 0) or (int(seat_id) > int(auditorium['row_count']) * int(auditorium['seats_per_row'])):
        print(f"\nSeat {seat_id} does not exist.")
        return

    if seat_id in get_reserved_seats(session_id):
        print(f"\nSeat {seat_id} is already reserved.")
        return

    try:
        p = r.pipeline()
        p.watch(f"{session_id}:reserved_seats")
        p.multi()
        #time.sleep(2)

        ticket_data = {
            'session_id': session_id,
            'seat_id': seat_id
        }

        ticket_id = "ticket" + str(r.scard("tickets"))

        p.hset(ticket_id, mapping=ticket_data)
        p.sadd("tickets",  ticket_id)

        p.execute()
        r.sadd(f"{session_id}:reserved_seats", seat_id)
    except redis.WatchError:
        print("Retry the transaction please")
        return


def get_ticket(ticket_id):
    ticket_id = r.hgetall(ticket_id)
    if ticket_id:
        return {key.decode(): value.decode() for key, value in ticket_id.items()}
    else:
        return None
