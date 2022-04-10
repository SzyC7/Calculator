def calculate(x, y, operation):
    operations = {"1": lambda a, b: x + y, "2": lambda a, b: x - y, "3": lambda a, b: x * y, "4": lambda a, b: x/y, "5": lambda a, b: x % y}
    return operations[operation](x, y)


def main():
    print("Calculator")
    print("1. Adding")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percent")
    end = False
    while not end:
        a = int(input("Podaj pierwsza liczbę:"))
        b = int(input("Podaj drugą liczbę:"))
        operation = input("Wybierz działanie:")

        result = calculate(a, b, operation)
        logging.info(f"Result: {result}")



if __name__ == "__main__":
    main()
