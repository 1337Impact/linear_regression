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


def mean(arr):
    return sum(arr) / len(arr)


def calculateTheta():
    theta0, theta1 = 0, 0

    file_data = read_csv_file()
    x_data = file_data['km']
    y_data = file_data['price']

    x_mean = mean(x_data)
    y_mean = mean(y_data)
    a, b = 0, 0
    for i in range(len(x_data)):
        a += (x_data[i] - x_mean) * (y_data[i] - y_mean)
        b += (x_data[i] - x_mean)**2
    theta1 = a / b
    theta0 = y_mean - (theta1 * x_mean)
    return [theta0, theta1]


def main():
    theta = calculateTheta()
    print(f"theta0: {theta[0]}")
    print(f"theta1: {theta[1]}")


if __name__ == "__main__":
    main()
