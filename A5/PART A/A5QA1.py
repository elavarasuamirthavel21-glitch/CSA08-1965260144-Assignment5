import sqlite3

con = sqlite3.connect("airquality.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS readings (
    station TEXT,
    date TEXT,
    pm25 REAL,
    pm10 REAL,
    no2 REAL,
    temperature REAL
)
""")

data = [
    ("Adyar", "2026-10-01", 48, 80, 20, 30),
    ("Guindy", "2026-10-01", 95, 120, 35, 32),
    ("Adyar", "2026-10-02", 60, 90, 25, 29)
]

cur.executemany(
    "INSERT INTO readings VALUES (?, ?, ?, ?, ?, ?)",
    data
)

con.commit()

cur.execute("SELECT AVG(pm25) FROM readings")
print("Average PM2.5:", cur.fetchone()[0])

con.close()
