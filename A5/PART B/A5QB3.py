import pandas as pd
import sqlite3
import time

data = [
    ("Adyar", "2026-10-01", 48),
    ("Adyar", "2026-10-01", 60),
    ("Guindy", "2026-10-01", 95),
    ("Guindy", "2026-10-01", 85)
]

# Python loops
start = time.perf_counter()

result = {}

for station, day, pm in data:
    key = (station, day)

    if key not in result:
        result[key] = []

    result[key].append(pm)

for key in result:
    result[key] = sum(result[key]) / len(result[key])

print("Python:", result)
print("Loop Time:", time.perf_counter() - start)


# Pandas
start = time.perf_counter()

df = pd.DataFrame(
    data, columns=["station", "day", "pm25"]
)

print("Pandas:")
print(df.groupby(["station", "day"])["pm25"].mean())

print("Pandas Time:", time.perf_counter() - start)


# SQL
start = time.perf_counter()

con = sqlite3.connect(":memory:")

df.to_sql("aq", con, index=False)

query = """
SELECT station, day, AVG(pm25)
FROM aq
GROUP BY station, day
"""

print("SQL:", con.execute(query).fetchall())

print("SQL Time:", time.perf_counter() - start)

con.close()
