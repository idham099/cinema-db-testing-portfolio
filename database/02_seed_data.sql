INSERT INTO users (name, email) VALUES 
('Budi Santoso', 'budi@example.com'),
('Siti Aminah', 'siti@example.com');

INSERT INTO shows (movie_title, available_seats, ticket_price) VALUES 
('Avengers: Secret Wars', 10, 50000.00);

-- Booking 1: VALID (Beli 2 tiket @ 50.000 = Total 100.000)
INSERT INTO bookings (user_id, show_id, total_seats, total_amount) VALUES 
(1, 1, 2, 100000.00);

-- Booking 2: BUG FINANSIAL (Beli 2 tiket @ 50.000, tapi tersimpan Total 80.000 -> Ada selisih Rp 20.000)
INSERT INTO bookings (user_id, show_id, total_seats, total_amount) VALUES 
(2, 1, 2, 80000.00);