import numpy as np

# Data
x = np.array([-1.1, -0.3, 0.8, 1.9])
f_x = np.array([15.180, 10.962, 1.920, -2.040])

# Calculate coefficients of the interpolating polynomial
coefficients = np.polyfit(x, f_x, deg=len(x) - 1)

# Create a polynomial using coefficients
polynomial = np.poly1d(coefficients)

# Compute f'(x) and f''(x)
f_prime = np.polyder(polynomial)
f_double_prime = np.polyder(f_prime)

# f'(x) & f''(x) at x = 0
f_prime_0 = f_prime(0)
f_double_prime_0 = f_double_prime(0)

# Print
print("f'(0) =", f_prime_0)
print("f''(0) =", f_double_prime_0)