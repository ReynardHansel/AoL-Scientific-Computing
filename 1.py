import matplotlib.pyplot as plt
import numpy as np

years = np.array([1981, 1983, 1985, 1987, 1989, 1991, 1993, 1995, 1997, 1999])
temperatures = np.array([14.1999, 14.2411, 14.0342, 14.2696, 14.197, 14.3055, 14.1853, 14.3577, 14.4187, 14.3438])

x_hat = np.array([1988]) # For finding a single or specifics even year
x_hats = np.arange(1982, 2000, 2) # For finding all even years


def linear_interpolate(x, y, x_hats):
    n = len(x)
    results = []
    
    for x_hat in x_hats:
        for j in range(n-1):
            if x[j] <= x_hat and x[j+1] >= x_hat:
                i = j
        y_hat = y[i] + ((y[i+1] - y[i]) * (x_hat - x[i]) / (x[i+1] - x[i]))
        results.append(y_hat)
    
    return results

estimated_temperatures = linear_interpolate(years, temperatures, x_hats)

# Printing each value
print('Linear Spline Interpolation:')
for year, temperature in zip(x_hats, estimated_temperatures):
    print(f"Estimated temperature in {year}: {temperature:.4f} °C")
print('\n\n')

# Plot
plt.figure(figsize=(10, 8))
plt.plot(years, temperatures, "-ob", label="Given Data")
plt.plot(x_hats, estimated_temperatures, "ro", label="Estimated Temperatures")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Linear Interpolation")
plt.legend()

# Loop to print each value of the red dots
for x, y in zip(x_hats, estimated_temperatures):
    plt.text(x, y, f"{y:.2f}", ha="center", va="bottom")
    # ha --> align center
    # va --> display below dot
plt.show()



def quadratic_spline_interpolate(x, y, x_hat):
    n = len(x)

    results = []
    for x_val in x_hat:
        # Find the indices of the closest values for x1, x2, x3
        idx = np.argsort(np.abs(x - x_val))[:3]
        x1, x2, x3 = x[idx]
        y1, y2, y3 = y[idx]

        # Evaluate the quadratic spline at x_hat
        y_val = (y1 * ((x_val - x2) * (x_val - x3)) / ((x1 - x2) * (x1 - x3)) +
                 y2 * ((x_val - x1) * (x_val - x3)) / ((x2 - x1) * (x2 - x3)) +
                 y3 * ((x_val - x1) * (x_val - x2)) / ((x3 - x1) * (x3 - x2)))

        results.append(y_val)

    return results

estimated_temperatures = quadratic_spline_interpolate(years, temperatures, x_hats)

# Print each value
print('Quadratic Spline Interpolation:')
for year, temperature in zip(x_hats, estimated_temperatures):
    print(f"Estimated temperature in {year}: {temperature:.4f} °C")
print('\n\n')

# Plot
plt.figure(figsize=(10, 8))
plt.plot(years, temperatures, "-ob", label="Given Data")
plt.plot(x_hats, estimated_temperatures, "ro", label="Estimated Temperatures")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Quadratic Spline Interpolation")
plt.legend()

# Loop to print each value of the red dots
for x, y in zip(x_hats, estimated_temperatures):
    plt.text(x, y, f"{y:.2f}", ha="center", va="bottom")
plt.show()



def linear_regression(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x ** 2)

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept

slope, intercept = linear_regression(years, temperatures)
estimated_temperatures = slope * x_hats + intercept


# Print each values
for year, temperature in zip(x_hats, estimated_temperatures):
    print(f"Estimated temperature in {year}: {temperature:.4f} °C")

# Plot
plt.figure(figsize=(10, 8))
plt.plot(years, temperatures, "bo", label="Given Data")
plt.plot(x_hats, estimated_temperatures, "ro", label="Estimated Temperatures")
plt.plot(years, linear_regression(years, temperatures)[0] * years + linear_regression(years, temperatures)[1], "--g", label="Regression Line")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Least Squares Regression")
plt.legend()

for x, y in zip(x_hats, estimated_temperatures):
    plt.text(x, y, f"{y:.2f}", ha="center", va="bottom")
plt.show()
