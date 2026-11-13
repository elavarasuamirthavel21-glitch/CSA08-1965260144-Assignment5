import time
import cProfile
import logging

logging.basicConfig(level=logging.INFO)

def clean_data(data):
    result = []

    for x in data:
        assert isinstance(x, int)

        if x >= 0:
            result.append(x)

    return result

data = [10, 20, -5, 30]

start = time.perf_counter()

print(clean_data(data))

end = time.perf_counter()

logging.info("Cleaning completed")

print("Execution Time:", end - start)

cProfile.run("clean_data(data)")
