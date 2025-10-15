def main():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    c = int(input("Enter Third Number: "))

    print(a, b, c)
    add = a + b + c
    mul = a * b * c
    power = (a**b) ** c # alternative, power = pow(pow(a, b), c)
    rem = a // b
    print(add, mul, power, rem)

if __name__ == "__main__":
    main()