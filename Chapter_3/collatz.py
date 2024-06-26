import sys


def main_loop():
    while True:
        inputErrorMessage = "Invalid entry: Enter a positive integer value only."
        try:
            number = int(input("Enter number: "))
            if number <= 0:
                print(inputErrorMessage)
                continue
            else:
                break
        except ValueError:
            print(inputErrorMessage)

    while number != 1:
        try:
            number = collatz(number)
            print(number)

        except KeyboardInterrupt:
            break

    sys.exit()


def collatz(number):
    "Print a Collatz Sequence until function end or interrupt."
    if number % 2 == 0:
        new_number = number // 2
        print(f"{number} // 2 = ", end="")
    else:
        new_number = 3 * number + 1
        print(f"3 * {number} + 1 = ", end="")

    return new_number


if __name__ == "__main__":
    main_loop()
