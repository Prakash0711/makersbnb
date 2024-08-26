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
    booking_date date,
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

INSERT INTO spaces (address, description, price, host_id) VALUES
('123 Main St', 'Cozy apartment in the heart of downtown', 100, 1),
('456 Elm St', 'Spacious loft with city views', 150, 2),
('789 Oak St', 'Charming cottage near the beach', 120, 3),
('321 Pine St', 'Modern studio with rooftop access', 80, 4);

INSERT INTO bookings (host_id, guest_id, space_id, booking_date, booking_status) VALUES
(1, 2, 1, '2024-05-10', 'approved'),
(2, 3, 2, '2024-05-15', 'pending'),
(3, 4, 3, '2024-05-20', 'denied'),
(4, 1, 4, '2024-05-25', 'approved');