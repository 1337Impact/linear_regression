from utils import read_csv_file


def sumOfSquaredResiduals(theta0, theta1, x_data, y_data):
    """calculate function error using sum of squared residuals algorithm

    Args:
        theta0 (number)
        theta1 (number)
        x_data (number[])
        y_data (number[])

    Returns:
        error value.
    """
    s = 0
    for i in range(len(x_data)):
        s += pow(y_data[i] - (theta0 + (theta1 * x_data[i])), 2)
    return s


def main():
    file_data = read_csv_file()
    x_data = file_data['km']
    y_data = file_data['price']

    theta0 = float(input("Enter theta0:"))
    theta1 = float(input("Enter theta1:"))

    print("SSR:", sumOfSquaredResiduals(theta0, theta1, x_data, y_data))


if __name__ == "__main__":
    main()
