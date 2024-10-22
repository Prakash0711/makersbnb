DROP TABLE IF EXISTS bookings cascade;
DROP TABLE IF EXISTS spaces cascade;
DROP TABLE IF EXISTS users cascade;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TYPE IF EXISTS status;
-- DROP CONSTRAINT IF EXISTS fk_guest;
-- DROP CONSTRAINT IF EXISTS fk_user;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username text UNIQUE,
    user_password text,
    email text UNIQUE,
    full_name text
    );



CREATE TABLE IF NOT EXISTS spaces (
    id SERIAL PRIMARY KEY,
    address text UNIQUE,
    city text,
    description text,
    price decimal,
    host_id int,
    constraint fk_user foreign key(host_id)
        references users(id)
        on delete cascade
    );

CREATE TYPE status AS ENUM('pending', 'approved', 'denied');

CREATE TABLE IF NOT EXISTS bookings (
    id SERIAL PRIMARY KEY,
    host_id int,
    guest_id int,
    space_id int,
    booking_date_start date,
    booking_date_end date,
    booking_status status,
    constraint fk_guest foreign key(guest_id)
        references users(id)
        on delete cascade,
    constraint fk_host foreign key(host_id)
        references users(id)
        on delete cascade,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade
    );



INSERT INTO users (username, user_password, email, full_name) VALUES
('john_doe', 'password123', 'john@example.com', 'John Doe'),
('jane_smith', 'securepass', 'jane@example.com', 'Jane Smith'),
('mike_jones', 'mikepass', 'mike@example.com', 'Mike Jones'),
('sara_williams', 'sara123', 'sara@example.com', 'Sara Williams');

INSERT INTO spaces (address, city, description, price, host_id) VALUES
('221B Baker Street', 'London', 'A classic flat in the heart of London', 180.00, 1),
('10 Downing Street', 'London', 'A historic townhouse with a political twist', 300.00, 2),
('15 Abbey Road', 'Liverpool', 'A modern apartment near famous recording studios', 120.50, 3),
('77 Canongate', 'Edinburgh', 'A charming flat on the Royal Mile', 175.75, 4),
('50 Castle Street', 'Edinburgh', 'An apartment with views of Edinburgh Castle', 220.00, 3),
('12 Kings Road', 'Brighton', 'A beachfront apartment with stunning sea views', 190.00, 2),
('34 Park Lane', 'Cardiff', 'A cozy apartment near Cardiff Castle', 140.99, 1),
('8 Duke Street', 'Glasgow', 'A stylish flat in the heart of Glasgow', 160.00, 2),
('3 St. Peter’s Avenue', 'Bristol', 'A quirky flat in Bristol’s creative quarter', 210.45, 3),
('22 High Street', 'Manchester', 'A chic city apartment near the Northern Quarter', 195.00, 4);


INSERT INTO bookings (host_id, guest_id, space_id, booking_date_start, booking_date_end, booking_status) VALUES
(1, 2, 1, '2024-05-10', '2024-05-12', 'approved'),
(2, 3, 2, '2024-05-15', '2024-05-17', 'pending'),
(3, 4, 3, '2024-05-20', '2024-05-22', 'denied'),
(4, 1, 4, '2024-05-25', '2024-05-27', 'approved');