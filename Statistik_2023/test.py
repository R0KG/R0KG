import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mean = 100
std_dev = 15
confidence_level = 0.95

# Calculate the critical value at the given confidence level
critical_value = norm.ppf(confidence_level, mean, std_dev)

# Set up a range of x values for the normal distribution curve
x_values = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
y_values = norm.pdf(x_values, mean, std_dev)

# Plot the normal distribution curve
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Normal Distribution')

# Fill the area for the significance level
plt.fill_between(x_values, y_values, where=(x_values > critical_value), color='red', alpha=0.5, label='95th Percentile')

# Draw a line for the critical value
plt.axvline(critical_value, color='black', linestyle='dashed', label=f'Critical Value: {critical_value:.2f}')

# Annotate the critical value on the plot
plt.text(critical_value, plt.ylim()[1]*0.1, f'{critical_value:.2f}', ha='center')

# Add titles and labels
plt.title('Normal Distribution (mean = 100, std = 15)')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
