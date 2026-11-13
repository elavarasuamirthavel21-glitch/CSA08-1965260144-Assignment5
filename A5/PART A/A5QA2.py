import statistics

data = [48, 95, 121, 60, 80]

minimum = min(data)
maximum = max(data)

normalised = [
    round((x - minimum) / (maximum - minimum), 3)
    for x in data
]

mean = statistics.mean(data)
std = statistics.stdev(data)

standardised = [
    round((x - mean) / std, 3)
    for x in data
]

print("Normalised:", normalised)
print("Standardised:", standardised)
