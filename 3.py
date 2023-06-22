import numpy as np

def riemann(a, b, h, t, v, mode='left'):
    i = 0
    j = len(t) - 1
    y = 0

    if mode == 'left':
        for k in v[i:j]:
            y += h * k
    elif mode == 'right':
        for k in v[i+1 : j+1]:
            y += h * k

    return y

def trapezoid(a, b, h, t, v):
    i = 0
    j = len(t) - 1
    n = 0

    for k in v[i+1 : j]:
        n += k

    return (v[i] + (2*n) + v[j]) * (h/2)

def simpsons(a, b, h, t, v):
    i = 0
    j = len(t) - 1
    n = len(t)

    if n < 3:
        print('Data range is too small')
        return -1
    
    # Rule 1/3 (Interval = even, length = odd)
    if n % 2 != 0:

        sum1 = 0
        for k in v[i+1 : j : 2]:
            sum1 += k
        
        sum2 = 0
        for k in v[i+2 : j-1 : 2]:
            sum2 += k

        y = (v[i] + (4*sum1) + (2*sum2) + v[j]) * (h/3)

    # Rule 3/8
    elif n % 2 == 0:
        sum3 = (v[i] + (3 * v[i+1]) + (3 * v[i+2]) + v[i+3]) * ((3*h) / 8)

        # 1/3 rules
        v_new = v[i+3 : j+1] # --> remaining data

        sum1 = 0
        for k in v_new[1 : -1 : 2]:
            sum1 += k
        
        sum2 = 0
        for k in v_new[2 : -2 : 2]:
            sum2 += k

        y = sum3 + ((h/3) * (v_new[0] + (4*sum1) + (2*sum2) + v_new[-1]))
    
    return y

# Define the function f(x)
def f(x):
    return x**3 - 0.3*x**2 - 8.56*x + 8.448

# Define the interval [a, b]
a = 0
b = 2 * np.pi

# Generate evenly spaced grid points
num_points = 20
t = np.linspace(a, b, num_points)
v = f(t)

# Calculate the step size
h = (b - a) / (num_points - 1)

# Calculate the integral using different methods
riemann_integral_left = riemann(a, b, h, t, v)
riemann_integral_right = riemann(a, b, h, t, v, mode='right')
trapezoid_integral = trapezoid(a, b, h, t, v)
simpsons_integral = simpsons(a, b, h, t, v)

# Print the results
print("Riemann Integral (Left):", riemann_integral_left)
print("Riemann Integral (Right):", riemann_integral_right)
print("Trapezoid Rule:", trapezoid_integral)
print("Simpson's Rule:", simpsons_integral)


###############################  C  ###########################################


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


###############################  D  ###########################################

# Define analytic functions for f'(x) & f''(x)
def f_prime_init(x):
    return 3*x**2 - 0.6*x - 8.56

def f_double_prime_init(x):
    return 6*x - 0.6

# Calculate when x = 0
f_prime_initial_0 = f_prime_init(0)
f_double_prime_initial_0 = f_double_prime_init(0)

# Calculate accuracy (absolute(numerical - analytic))
accuracy_f_prime = abs(f_prime_0 - f_prime_initial_0)
accuracy_f_double_prime = abs(f_double_prime_0 - f_double_prime_initial_0)

#print
print("Accuracy of f'(0) compared to the initial function:", accuracy_f_prime)
print("Accuracy of f''(0) compared to the initial function:", accuracy_f_double_prime)