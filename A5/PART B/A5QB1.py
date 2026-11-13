import csv
import io

RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Guindy,2026-10-04,1200
"""

def load_clean(text):
    rows = []

    reader = csv.DictReader(io.StringIO(text))

    for row in reader:
        value = row["pm25"]

        if value and value != "NA":
            pm = float(value)

            if 0 <= pm <= 999:
                rows.append((row["station"], row["date"], pm))

    return rows


def min_max(values):
    low = min(values)
    high = max(values)

    return [
        round((v - low) / (high - low), 3)
        for v in values
    ]


clean = load_clean(RAW)

print("Clean Data:", clean)
print("Normalised:", min_max([pm for _, _, pm in clean]))
