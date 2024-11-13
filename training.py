import sys
from utils import read_csv_file


def estimatePrice(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)


def calcTheta0(x_data, y_data, theta0, theta1, learning_rate):
    s = 0
    for i in range(len(x_data)):
        s += estimatePrice(x_data[i], theta0, theta1) - y_data[i]
    return learning_rate * s / len(x_data)


def calcTheta1(x_data, y_data, theta0, theta1, learning_rate):
    s = 0
    for i in range(len(x_data)):
        s += (estimatePrice(x_data[i], theta0, theta1) - y_data[i]) * x_data[i]
    return learning_rate * s / len(x_data)


def gradientDescent(x_data, y_data, theta0=0, theta1=0, iteration=0):
    """this function calculate theta0 and theta1 using gradient descent

    Returns:
        [theta0, theta1]
    """
    learning_rate = 0.01
    if iteration == 200:
        return [theta0, theta1]

    tmp_theta0 = calcTheta0(
        x_data, y_data, theta0, theta1, learning_rate)
    tmp_theta1 = calcTheta1(
        x_data, y_data, theta0, theta1, learning_rate)

    theta0 -= tmp_theta0
    theta1 -= tmp_theta1

    return gradientDescent(x_data, y_data, theta0, theta1, iteration + 1)


def scaleData(data, scaler):
    return [e * scaler for e in data]


def main():
    sys.setrecursionlimit(100000)

    # read data from csv
    file_data = read_csv_file()
    x_data = file_data['km']
    y_data = file_data['price']

    # scale data down to avoid overflow
    x_data = scaleData(x_data, 0.0001)
    y_data = scaleData(y_data, 0.0001)

    # calculate thera using Gradiant descent
    print("Gradiant descent: ")
    theta = gradientDescent(x_data, y_data)
    print(f"theta0: {theta[0] * 10000}")
    print(f"theta1: {theta[1]}")


if __name__ == "__main__":
    main()
