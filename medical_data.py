import matplotlib.pyplot as plt
import numpy as np

# Simulate heart rate data (beats per minute over time)
np.random.seed(42)  # For reproducibility
time = np.arange(0, 60, 0.1)  # 60 seconds, sampled every 0.1s
heart_rate = 70 + 10 * np.sin(time) + \
    np.random.normal(0, 5, len(time))  # Simulated HR

# Define normal range (e.g., 60-100 bpm)
normal_range = (60, 100)
anomalies = (heart_rate < normal_range[0]) | (heart_rate > normal_range[1])

# Plot the heart rate
plt.figure(figsize=(10, 6))
plt.plot(time, heart_rate, label="Heart Rate (BPM)", color="blue")
plt.fill_between(time, normal_range[0], normal_range[1],
                 color="green", alpha=0.2, label="Normal Range (60-100 BPM)")

# Highlight anomalies
plt.scatter(time[anomalies], heart_rate[anomalies],
            color="red", label="Anomalies", s=50)

# Add labels and title
plt.xlabel("Time (seconds)")
plt.ylabel("Heart Rate (BPM)")
plt.title("Simulated Heart Rate Monitoring")
plt.legend()
plt.grid(True)
plt.show()

# Calculate basic stats
avg_hr = np.mean(heart_rate)
max_hr = np.max(heart_rate)
min_hr = np.min(heart_rate)
anomaly_count = np.sum(anomalies)

print(f"Average Heart Rate: {avg_hr:.1f} BPM")
print(f"Max Heart Rate: {max_hr:.1f} BPM")
print(f"Min Heart Rate: {min_hr:.1f} BPM")
print(f"Number of Anomalies: {anomaly_count}")
