from connection import *
from session import *
from auditorium import *
import time
import re


def buy_ticket(session_id, seat_id):

    session = get_session(session_id)

    if session is None:
        print("\nThis session does not exist.")
        return

    auditorium = get_auditorium(session["auditorium"])

    if (int(seat_id[1:]) < 1) or (int(seat_id[1:]) > int(auditorium['row_count'])):
        print(f"\nSeat {seat_id} does not exist.")
        return

    # Seat number from LN format
    seat_number = (ord(seat_id[0]) - 65) * int(auditorium['seats_per_row']) + int(seat_id[1:])

    if seat_number > int(auditorium['seats_per_row'])*int(auditorium['row_count']):
        print(f"\nSeat {seat_id} does not exist.")
        return

    if str(seat_number) in get_reserved_seats(session_id):
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
        p.sadd(f"{session_id}:reserved_seats", seat_number)
        p.execute()
    except redis.WatchError:
        print("Transaction failed, please try again.")
        return


def get_ticket(ticket_id):
    ticket_id = r.hgetall(ticket_id)
    if ticket_id:
        return {key.decode(): value.decode() for key, value in ticket_id.items()}
    else:
        return None