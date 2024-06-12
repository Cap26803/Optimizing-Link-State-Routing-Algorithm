import matplotlib.pyplot as plt

# Data
nodes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
baseline_times = [2.5, 5.3, 7.8, 11.2, 14.5, 18.2, 22.0, 25.5, 29.1, 33.0, 37.5, 41.2, 45.0, 49.2, 53.5, 58.0, 62.5, 67.2, 72.0, 76.8]
optimized_times = [1.2, 2.6, 3.8, 5.4, 7.2, 9.0, 11.5, 13.8, 16.2, 18.5, 21.2, 24.0, 27.3, 30.1, 33.5, 37.2, 41.0, 45.5, 50.2, 55.0]
time_difference = [1.3, 2.7, 4.0, 5.8, 7.3, 9.2, 10.5, 11.7, 12.9, 14.5, 16.3, 17.2, 17.7, 19.1, 20.0, 20.8, 21.5, 21.7, 21.8, 21.8]

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(nodes, baseline_times, label='Baseline Algorithm Time (seconds)', marker='o')
plt.plot(nodes, optimized_times, label='Optimized Algorithm Time (seconds)', marker='o')
plt.plot(nodes, time_difference, label='Time Difference (seconds)', marker='o')

plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Baseline and Optimized Algorithm Times')
plt.legend()
plt.grid(True)
plt.xticks(nodes, rotation=45)
plt.tight_layout()

# Display the plot
plt.show()