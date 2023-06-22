import math

def taylor_series(term_fn, x, n):
    series_sum = 0
    for i in range(n):
        term = term_fn(x, i)
        series_sum += term
    return series_sum

def sin(x, i):
    return (-1) ** i * x ** (2 * i + 1) / math.factorial(2 * i + 1)

def cos(x, i):
    return (-1) ** i * x ** (2 * i) / math.factorial(2 * i)

def sin_cos(x, i):
    return (-1) ** i * x ** (2 * i + 1) / math.factorial(2 * i + 1)

# x = 0  # Centered around 0 --> untuk soal a
x = math.pi / 4 #c --> untuk soal c
n = 4  # Fourth-order

sin_approx = taylor_series(sin, x, n)
cos_approx = taylor_series(cos, x, n)
sin_cos_approx = taylor_series(sin_cos, x, n)

print("sin(x) =", sin_approx)
print("cos(x) =", cos_approx)
print("sin(x)cos(x) =", sin_cos_approx)

sin_error = abs(math.sin(x) - sin_approx)
cos_error = abs(math.cos(x) - cos_approx)
sin_cos_error = abs((math.sin(x) * math.cos(x)) - sin_cos_approx)

print("The error for sin(x) is:", sin_error)
print("The error for cos(x) is:", cos_error)
print("The error for sin(x)cos(x) is:", sin_cos_error)