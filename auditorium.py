from connection import *


def add_auditorium(row_count, seats_per_row):
    if not row_count.isdigit() or not seats_per_row.isdigit(): 
        print("\nInvalid input.")
        return

    if row_count > 20 or seats_per_row > 99:
        print("\nToo many seats.")
        return
    
    auditorium_data = {
        'row_count': row_count,
        'seats_per_row': seats_per_row,
    }

    auditorium_id = "a" + str(r.scard("auditoriums"))
    r.hset(auditorium_id, mapping=auditorium_data)
    r.sadd("auditoriums",  auditorium_id)


def get_auditorium(auditorium_id):
    auditorium_data = r.hgetall(auditorium_id)
    if auditorium_data:
        return {key.decode(): value.decode() for key, value in auditorium_data.items()}
    else:
        return None
