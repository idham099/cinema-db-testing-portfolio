import psycopg2
import pytest

DB_CONFIG = {
    "dbname": "cinema_booking",
    "user": "qa_tester",
    "password": "secretpassword",
    "host": "localhost",
    "port": "5432"
}

@pytest.fixture
def db_conn():
    conn = psycopg2.connect(**DB_CONFIG)
    yield conn
    conn.close()

def test_negative_seats_should_fail(db_conn):
    """Mencoba memasukkan jumlah kursi negatif. Database harus MENOLAK (Throw Error)."""
    cursor = db_conn.cursor()
    with pytest.raises(psycopg2.errors.CheckViolation):
        cursor.execute(
            "INSERT INTO shows (movie_title, available_seats, ticket_price) VALUES (%s, %s, %s);",
            ("Film Test Fail", -5, 50000.00)
        )
    db_conn.rollback()

def test_invalid_user_booking_should_fail(db_conn):
    """Mencoba transaksi dengan ID user yang tidak terdaftar. Database harus MENOLAK (FK Error)."""
    cursor = db_conn.cursor()
    with pytest.raises(psycopg2.errors.ForeignKeyViolation):
        cursor.execute(
            "INSERT INTO bookings (user_id, show_id, total_seats, total_amount) VALUES (%s, %s, %s, %s);",
            (9999, 1, 1, 50000.00)
        )
    db_conn.rollback()