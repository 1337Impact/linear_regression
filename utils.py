import csv


def read_csv_file():
    km = []
    price = []
    with open('data.csv', mode='r')as file:
        csvFile = csv.reader(file)
        for i, lines in enumerate(csvFile):
            if i == 0:
                continue
            km.append(int(lines[0]))
            price.append(int(lines[1]))
    return {'km': km, 'price': price}


def leastSquares(x_data, y_data):
    """this function calculate theta0 and theta1 using least squares algorithm

    Returns:
        [theta0, theta1]
    """
    x_mean = sum(x_data) / len(x_data)
    y_mean = sum(y_data) / len(y_data)
    a, b = 0, 0
    for i in range(len(x_data)):
        a += (x_data[i] - x_mean) * (y_data[i] - y_mean)
        b += (x_data[i] - x_mean)**2
    theta1 = a / b
    theta0 = y_mean - (theta1 * x_mean)
    return [theta0, theta1]
