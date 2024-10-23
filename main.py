def estimatePrice(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)


def main():
    theta0 = 0
    theta1 = 0

    mileage = input("Enter mileage:")
    if mileage.isnumeric():
        print(estimatePrice(int(mileage), theta0, theta1))
    else:
        print("Error: invalid value")


if __name__ == "__main__":
    main()
