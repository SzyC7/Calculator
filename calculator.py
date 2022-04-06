def calculate(x, y, operation):
    operations = {"1": lambda a, b: x + y, "2": lambda a, b: x - y, "3": lambda a, b: x * y, "4": lambda a, b: x/y, "5": lambda a, b: x % y}
    return operations[operation](x, y)

import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def main():
    logging.info("Kalkulator")
    logging.info("1. Dodawanie")
    logging.info("2. Odejmowanie")
    logging.info("3. Mnożenie")
    logging.info("4. Dzielenie")
    logging.info("5. Procent")
    end = False
    while not end:
        a = int(input("Podaj pierwsza liczbę:"))
        b = int(input("Podaj drugą liczbę:"))
        działanie = input("Wybierz działanie:")

        print(calculate(a, b, działanie))



if __name__ == "__main__":
    main()
