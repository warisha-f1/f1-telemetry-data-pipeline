import sqlite3

def create_database():
    # Connect to (or create) the SQLite database file
    conn = sqlite3.connect('f1_telemetry.db')
    cursor = conn.cursor()

    # Enable Foreign Key support in SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Create RACES Table (Metadata)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS races (
            race_key INTEGER PRIMARY KEY,
            year INTEGER,
            grand_prix TEXT,
            session_type TEXT,
            date TEXT
        )
    ''')

    # 2. Create LAPS Table (Aggregated Data)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS laps (
            lap_id INTEGER PRIMARY KEY AUTOINCREMENT,
            race_key INTEGER,
            driver_id TEXT,
            lap_number INTEGER,
            lap_time_seconds REAL,
            compound TEXT,
            median_pace REAL,
            FOREIGN KEY (race_key) REFERENCES races (race_key)
        )
    ''')

    # 3. Create TELEMETRY Table (High-Frequency Data)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telemetry (
            telemetry_id INTEGER PRIMARY KEY AUTOINCREMENT,
            lap_id INTEGER,
            time_ms INTEGER,
            speed_kph INTEGER,
            throttle REAL,
            brake REAL,
            gear INTEGER,
            FOREIGN KEY (lap_id) REFERENCES laps (lap_id)
        )
    ''')

    conn.commit()
    print("Database and Tables created successfully!")
    conn.close()

if __name__ == "__main__":
    create_database() 