DROP TABLE IF EXISTS bookings cascade;
DROP TABLE IF EXISTS spaces cascade;
DROP TABLE IF EXISTS users cascade;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TYPE IF EXISTS booking_status;
-- DROP CONSTRAINT IF EXISTS fk_guest;
-- DROP CONSTRAINT IF EXISTS fk_user;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username text,
    user_password text,
    email text,
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
    booking_status  status,
    constraint fk_guest foreign key(guest_id)
        references users(id)
        on delete cascade,
    constraint fk_host foreign key(host_id)
        references users(id)
        on delete cascade,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade
    -- CONSTRAINT valid_booking_status
    --     CHECK (current_booking_status IN ('pending', 'approved', 'denied'))
    );