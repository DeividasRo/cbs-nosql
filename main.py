from auditorium import *
from session import *
from booking import *


def display_seats(session_id):
    session_data = get_session(session_id)
    if session_data is None:
        print("\nThis session does not exist.")
        return
    auditorium = get_auditorium(session_data['auditorium'])
    seats_per_row = int(auditorium['seats_per_row'])
    total_seats = int(auditorium['row_count']) * seats_per_row

    reserved_seats = get_reserved_seats(session_id)

    print('\n     ', end=' ')
    print('Reserved seats are marked with X symbol')

    print('\n     ', end=' ')
    for col_num in range(1, seats_per_row + 1):
        print('{:2d}'.format(col_num), end=' ')
    print()

    for seat_num in range(1, total_seats + 1):
        if seat_num % seats_per_row == 1:
            row_letter = chr(65 + (seat_num - 1) // seats_per_row)
            print(f'Row {row_letter}:', end=' ')

        if str(seat_num) in reserved_seats:
            print('X ', end=' ')
        else:
            print('- ', end=' ')

        if seat_num % seats_per_row == 0:
            print()
    print()


def display_auditoriums():
    print("ALL EXISTING AUDITORIUMS")
    auditoriums = list(r.smembers("auditoriums"))
    for auditorium in auditoriums:
        auditorium_details = get_auditorium(auditorium)
        print(f"id: {auditorium.decode('utf-8')}")
        if auditorium_details:
            for key, value in auditorium_details.items():
                print(f"{key}: {value}")
            print()


def display_sessions():
    print("ALL EXISTING SESSIONS")
    sessions = list(r.smembers("sessions"))
    for session in sessions:
        session_details = get_session(session)
        print(f"id: {session.decode('utf-8')}")
        if session_details:
            for key, value in session_details.items():
                print(f"{key}: {value}")
            print()


def display_tickets():
    print("ALL PURCHASED TICKETS")
    tickets = list(r.smembers("tickets"))
    for ticket in tickets:
        ticket_details = get_ticket(ticket)
        print(f"id: {ticket.decode('utf-8')}")
        if ticket_details:
            for key, value in ticket_details.items():
                print(f"{key}: {value}")
            print()


def main():
    print("Welcome to the Cinema Booking System!")

    while True:
        print("\nSelect an action:")
        print("1 - Add an auditorium")
        print("2 - Add a session")
        print("3 - Buy a ticket")
        print("4 - Display all auditoriums")
        print("5 - Display all sessions")
        print("6 - Display all tickets")
        print("7 - Display all seats of a session")
        x = input()
        if x == '1':
            add_auditorium(input("Enter row count (1-20): "),
                           input("Enter seat per row (1-99): "))
        elif x == '2':
            add_session(input("Enter session date (YYYY-MM-DD): "),
                        input("Enter session time (HH:MM): "),
                        input("Enter movie title: "),
                        input("Enter auditorium: "))
        elif x == '3':
            s_id = input("Enter session id: ")
            display_seats(s_id)
            buy_ticket(s_id,
                       input("Enter seat number: "))
        elif x == '4':
            display_auditoriums()
        elif x == '5':
            display_sessions()
        elif x == '6':
            display_tickets()
        elif x == '7':
            display_seats(input("Enter session id: "))
        elif x.lower() == 'q':
            break


if __name__ == "__main__":
    main()
