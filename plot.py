import matplotlib.pyplot as plt
from utils import read_csv_file


def l_func(x, b, m):
    return b + (x * m)


def plotData(x_data, y_data):
    plt.figure(figsize=(10, 6))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot Data')
    plt.scatter(x_data, y_data, color='red', label='Data points')

    y_slope = [l_func(x, 8499.59964993295, -0.021448963591700208)
               for x in x_data]
    plt.plot(x_data, y_slope, color='blue', label='Slope line')

    plt.legend()
    plt.grid(True)

    plt.show()


def main():
    file_data = read_csv_file()
    x_data = file_data['km']
    y_data = file_data['price']
    plotData(x_data, y_data)


if __name__ == "__main__":
    main()
