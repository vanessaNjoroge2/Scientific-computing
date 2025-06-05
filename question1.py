import matplotlib.pyplot as plt

# Temperature readings over a week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [20, 21, 18, 24, 25, 23, 20]

plt.plot(days, temperatures, marker='o', linestyle='-', color='blue')
plt.title("Temperature Readings Over a Week")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
