-- Create HotelChains table
CREATE TABLE HotelChains (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    office_address VARCHAR(200) NOT NULL
); -- done

CREATE TABLE HotelChainContact (
    id SERIAL PRIMARY KEY,
    hotel_chain_id INT NOT NULL,
    type VARCHAR(20) NOT NULL,
    content VARCHAR(100) NOT NULL,
    CONSTRAINT fk_hotel_chain
        FOREIGN KEY (hotel_chain_id)
        REFERENCES HotelChains(id)
        ON DELETE CASCADE
); -- done

CREATE TABLE Hotels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    star_rating INT NOT NULL CHECK (star_rating BETWEEN 1 AND 5),
    hotel_chain_id INT NOT NULL,
    CONSTRAINT fk_hotel_chain
        FOREIGN KEY (hotel_chain_id)
        REFERENCES HotelChains(id)
        ON DELETE CASCADE
); -- done

CREATE TABLE HotelContact (
    id SERIAL PRIMARY KEY,
    hotel_id INT NOT NULL,
    type VARCHAR(20) NOT NULL,
    content VARCHAR(100) NOT NULL,
    CONSTRAINT fk_hotel
        FOREIGN KEY (hotel_id)
        REFERENCES Hotels(id)
        ON DELETE CASCADE
); -- done


CREATE TABLE Rooms (
    id SERIAL PRIMARY KEY,
    room_number INT NOT NULL,
    capacity INT NOT NULL CHECK (capacity > 0),
    price NUMERIC(10, 2) NOT NULL CHECK (price > 0),
    is_extendable BOOLEAN NOT NULL,
    view_types VARCHAR(100),
    amenities VARCHAR(200) NOT NULL,
    problems VARCHAR(200),
    hotel_id INT NOT NULL,
    is_available BOOLEAN DEFAULT TRUE
    CONSTRAINT fk_hotel
        FOREIGN KEY (hotel_id)
        REFERENCES Hotels(id)
        ON DELETE CASCADE,

); -- done

CREATE TABLE Customers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    registration_date DATE NOT NULL
); -- done

CREATE TABLE CustomerIdentification (
    id SERIAL PRIMARY KEY,
    id_type VARCHAR(50) NOT NULL,
    content VARCHAR(50) NOT NULL,
    customer_id INTEGER NOT NULL,
    driver_license VARCHAR(15) NOT NULL,
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES Customers(id)
        ON DELETE CASCADE
); -- done

CREATE TABLE EmployeeIdentification (
    id SERIAL PRIMARY KEY,
    id_type VARCHAR(50) NOT NULL,
    content VARCHAR(50) NOT NULL,
    employee_id INTEGER NOT NULL,
    CONSTRAINT fk_employee
        FOREIGN KEY (employee_id)
        REFERENCES Employees(id)
        ON DELETE CASCADE
); -- done

CREATE TABLE Employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    role VARCHAR(50) NOT NULL,
    hotel_id INT NOT NULL,
    CONSTRAINT fk_hotel
        FOREIGN KEY (hotel_id)
        REFERENCES Hotels(id)
        ON DELETE CASCADE
); -- done

CREATE TABLE Rentings (
    id SERIAL PRIMARY KEY,
    was_booked BOOLEAN NOT NULL,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    payment_status VARCHAR(50) NOT NULL,
    customer_id INT NOT NULL,
    room_id INT NOT NULL,
    employee_id INT NOT NULL,
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES Customers(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_room
        FOREIGN KEY (room_id)
        REFERENCES Rooms(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_employee
        FOREIGN KEY (employee_id)
        REFERENCES Employees(id)
        ON DELETE CASCADE,
    CONSTRAINT invalid_date
        CHECK (check_in_date < check_out_date)
);--done