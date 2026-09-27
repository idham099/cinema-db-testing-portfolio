import psycopg2

DB_CONFIG = {
    "dbname": "cinema_booking",
    "user": "qa_tester",
    "password": "secretpassword",
    "host": "localhost",
    "port": "5432"
}

def test_financial_reconciliation():
    """
    Memastikan total_amount di tabel 'bookings' persis sama dengan (total_seats * ticket_price).
    Jika ada selisih, tes akan FAILED dan melaporkan ID transaksi bermasalah.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    query = """
        SELECT 
            b.id AS booking_id,
            b.total_amount AS recorded_amount,
            (b.total_seats * s.ticket_price) AS expected_amount,
            (b.total_amount - (b.total_seats * s.ticket_price)) AS discrepancy
        FROM bookings b
        JOIN shows s ON b.show_id = s.id
        WHERE b.total_amount <> (b.total_seats * s.ticket_price);
    """
    cursor.execute(query)
    discrepancies = cursor.fetchall()
    conn.close()

    # Jika list 'discrepancies' tidak kosong, berarti ditemukan bug selisih data
    assert len(discrepancies) == 0, f"DITEMUKAN BUG FINANSIAL! Detail: {discrepancies}"