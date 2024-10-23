import matplotlib.pyplot as plt


def l_func(x, m, b):
    return (x * m) + b


def mean(arr):
    return sum(arr) / len(arr)


def sumOfSquaredResiduals(intercept, slope, x_data, y_data):
    s = 0
    for i in range(len(x_data)):
        s += pow(y_data[i] - (intercept + (slope * x_data[i])), 2)
    return s


def calculate_derivatives(x_data, y_data):
    residuals = sumOfSquaredResiduals(intercept, slope, x_data, y_data)
    derivative_wrt_intercept = sp.diff(residuals, intercept)
    derivative_wrt_slope = sp.diff(residuals, slope)
    return derivative_wrt_intercept, derivative_wrt_slope

# def calcSlope(x_data, y_data, x_mean, y_mean):
#     a, b = 0, 0
#     for i in range(len(x_data)):
#         a += (x_data[i] - x_mean) * (y_data[i] - y_mean)
#         b += (x_data[i] - x_mean)**2
#     m = a / b
#     return m


x_data = [1, 2, 3]
y_data = [3, 5, 7]

intercept = [0.5, 1, 1.5, 2, 2.5, 3]
ssr = [sumOfSquaredResiduals(1, i, x_data, y_data) for i in intercept]


# plt.figure(figsize=(10, 6))

# plt.scatter(x_data, y_data, color='red', label='Data points')

# x_slope = [min(x_data) - 1, max(x_data) + 1]
# y_slope = [l_func(x, 60, 0) for x in x_data]
# plt.plot(x_data, y_slope, color='blue',
#          label='Slope line')
# y_slope = [l_func(x, 6, 0) for x in x_data]
# plt.plot(x_data, y_slope, color='red',
#          label='Slope line2')

# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Data Points and Slope Line')
# plt.legend()
# plt.grid(True)

# plt.show()


plt.figure(figsize=(10, 6))

plt.plot(intercept, ssr, color='blue',
         label='Slope line')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Points and Slope Line')
plt.legend()
plt.grid(True)

plt.show()
