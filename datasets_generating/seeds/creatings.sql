CREATE TABLE
    citizens (
        id TEXT,
        first_name TEXT,
        last_name TEXT,
        sex TEXT,
        birthday TEXT,
        age INTEGER,
        social_credit REAL
    );

CREATE TABLE
    id_cards (
        card_id TEXT,
        citizen_id TEXT,
        is_active BOOLEAN,
        FOREIGN KEY (citizen_id) REFERENCES citizens (id) ON DELETE CASCADE ON UPDATE NO ACTION
    );

CREATE TABLE
    addresses (
        address TEXT,
        lon_from REAL,
        lon_to REAL,
        lat_from REAL,
        lat_to REAL,
        note TEXT
    );

CREATE TABLE
    cameras (
        id INTEGER,
        lon REAL,
        lat REAL,
        address TEXT,
        FOREIGN KEY (address) REFERENCES addresses (address) ON DELETE CASCADE ON UPDATE NO ACTION
    );

CREATE TABLE
    camera_logs (
        id INTEGER,
        camera_id INTEGER,
        citizen_id TEXT,
        datetime TEXT,
        FOREIGN KEY (camera_id) REFERENCES cameras (id) ON DELETE CASCADE ON UPDATE NO ACTION,
        FOREIGN KEY (citizen_id) REFERENCES citizens (id) ON DELETE CASCADE ON UPDATE NO ACTION
    );

CREATE TABLE
    card_swipes (
        swipe_id INTEGER,
        card_id TEXT,
        datetime TEXT,
        FOREIGN KEY (card_id) REFERENCES id_cards (id) ON DELETE CASCADE ON UPDATE NO ACTION
    );

CREATE TABLE
    guard_logs (
        id INTEGER,
        datetime TEXT,
        event_type TEXT,
        action_taken TEXT,
        lon REAL,
        lat REAL
    );

CREATE TABLE
    safety_controls (key TEXT, value BOOLEAN);

CREATE TABLE
    system_audits_inner (id INTEGER, parent_id INTEGER, content TEXT);

CREATE TABLE
    system_audits (
        id INTEGER,
        log_date TEXT,
        content TEXT,
        "SHA-256" TEXT,
        is_flag_hidden BOOLEAN
    );

CREATE TABLE
    taxi_logs (
        trip_id INTEGER,
        citizen_id TEXT,
        trip_time TEXT,
        destination_lon REAL,
        destination_lat REAL,
        actual_dropoff_lon REAL,
        actual_dropoff_lat REAL,
        distance_offset_km REAL,
        FOREIGN KEY (citizen_id) REFERENCES citizens (id) ON DELETE CASCADE ON UPDATE NO ACTION
    );

CREATE TABLE
    missing_people (citizen_id TEXT, first_name TEXT, last_name TEXT);