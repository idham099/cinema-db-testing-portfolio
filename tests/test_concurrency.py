import threading
import psycopg2

DB_CONFIG = {
    "dbname": "cinema_booking",
    "user": "qa_tester",
    "password": "secretpassword",
    "host": "localhost",
    "port": "5432"
}

def attempt_booking(show_id, user_id, seats_to_book, results):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = False
        cursor = conn.cursor()

        # Gunakan Row-Level Locking (FOR UPDATE)
        cursor.execute("SELECT available_seats FROM shows WHERE id = %s FOR UPDATE;", (show_id,))
        available = cursor.fetchone()[0]

        if available >= seats_to_book:
            cursor.execute("UPDATE shows SET available_seats = available_seats - %s WHERE id = %s;", (seats_to_book, show_id))
            cursor.execute("INSERT INTO bookings (user_id, show_id, total_seats, total_amount) VALUES (%s, %s, %s, %s);",
                           (user_id, show_id, seats_to_book, 50000.00))
            conn.commit()
            results.append("SUCCESS")
        else:
            conn.rollback()
            results.append("NO_SEATS")
    except Exception as e:
        results.append(f"ERROR: {str(e)}")
    finally:
        conn.close()

def test_race_condition_seat_booking():
    """Memastikan dua transaksi yang diproses bersamaan tidak menyebabkan overbooking."""
    results = []
    # Jalankan 2 thread bersamaan mencoba memesan 10 kursi tersisa
    t1 = threading.Thread(target=attempt_booking, args=(1, 1, 10, results))
    t2 = threading.Thread(target=attempt_booking, args=(1, 2, 10, results))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    # Hanya 1 yang boleh SUCCESS, sisanya harus NO_SEATS
    assert results.count("SUCCESS") == 1
    assert results.count("NO_SEATS") == 1