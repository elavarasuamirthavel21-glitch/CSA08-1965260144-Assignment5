import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
pm25 = [48, 60, 55, 80, 70]

plt.plot(days, pm25, marker='o')
plt.title("Daily PM2.5 Trend")
plt.xlabel("Days")
plt.ylabel("PM2.5 Level")
plt.show()

stations = ["Adyar", "Guindy", "Padi"]
values = [48, 95, 70]

plt.bar(stations, values)
plt.title("Station Comparison")
plt.xlabel("Stations")
plt.ylabel("PM2.5")
plt.show()

temperature = [28, 30, 32, 29, 31]

plt.scatter(temperature, pm25)
plt.title("Temperature vs PM2.5")
plt.xlabel("Temperature")
plt.ylabel("PM2.5")
plt.show()
