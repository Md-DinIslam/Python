def main():
    # list..
    print("List")
    lst = [2, 'Din', 5]
    print(lst[0], lst[-1])
    print("\n")

    # set..
    print("Set")
    st = {3, 3, 1, 5}
    print(st)
    for x in st:
        print(x, end = " ")
    print("\n")

    # tupple..
    print("Tupple")
    tuple = (1, 3, 4) # value can't be change
    print(tuple[0], tuple[2])

    for x in tuple:
        print(x, end = " ")
    print("\n")

if __name__ == "__main__":
    main()