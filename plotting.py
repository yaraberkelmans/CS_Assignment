import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("istherecorrelation.csv", sep=";", decimal=",")

# Extract the two relevant columns 
x = df["WO [x1000]"]
y = df["NL Beer consumption [x1000 hectoliter]"]

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color="blue", alpha=0.7, label="Data")

# Fit and plot regression line
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color="red", label=f"Fit: y = {m:.2f}x + {b:.2f}")

# Labels and title
plt.xlabel("WO [x1000]")
plt.ylabel("NL Beer consumption [x1000 hectoliter]")
plt.title("Correlation between university graduates and beer consumption in NL")
plt.legend()

# Save to file (DPI=300)
plt.tight_layout()
plt.savefig("correlation_plot.png", dpi=300)
plt.show()
