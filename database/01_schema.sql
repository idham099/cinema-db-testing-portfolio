-- Tabel Pengguna
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Tabel Jadwal Film
CREATE TABLE shows (
    id SERIAL PRIMARY KEY,
    movie_title VARCHAR(150) NOT NULL,
    available_seats INT NOT NULL CHECK (available_seats >= 0),
    ticket_price NUMERIC(10, 2) NOT NULL CHECK (ticket_price > 0)
);

-- Tabel Transaksi Pemesanan
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    show_id INT REFERENCES shows(id) ON DELETE CASCADE,
    total_seats INT NOT NULL CHECK (total_seats > 0),
    total_amount NUMERIC(10, 2) NOT NULL CHECK (total_amount >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);