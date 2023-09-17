from connection import r
from auditorium import get_auditorium

def display_seats(auditorium_id):
    auditorium = get_auditorium(auditorium_id)
    if auditorium:
        row_count = int(auditorium['row_count'])
        seats_per_row = int(auditorium['seats_per_row'])
        total_seats = row_count * seats_per_row

        reserved_seats = set(map(int, r.smembers(f"{auditorium_id}:reserved_seats")))

        print('     ', end=' ')
        for col_num in range(1, seats_per_row + 1):
            print('{:2d}'.format(col_num), end=' ')
        print()

        for seat_num in range(1, total_seats + 1):
            if seat_num % seats_per_row == 1:
                row_letter = chr(65 + (seat_num - 1) // seats_per_row)
                print(f'Row {row_letter}:', end=' ')
            
            if seat_num in reserved_seats:
                print('X ', end=' ')
            else:
                print('- ', end=' ')
            
            if seat_num % seats_per_row == 0:
                print()

def reserve_seat(auditorium_id, row_number, seat_number):
    seats_per_row = int(get_auditorium(auditorium_id)['seats_per_row'])
    seat_number = (row_number - 1) * seats_per_row + seat_number
    
    reserved_seats_key = f"{auditorium_id}:reserved_seats"
    r.sadd(reserved_seats_key, seat_number)

if __name__ == "__main__":
    auditorium_id = "a0"

    row_number = 5
    seat_number = 9
    reserve_seat(auditorium_id, row_number, seat_number)
    
    print("Available and Reserved Seats for Auditorium (X - occupied):", auditorium_id)
    display_seats(auditorium_id)
