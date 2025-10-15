def main():
    lst = [2, 9, 5, 1, 1, 8]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if (lst[i] < lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    
    for x in lst:
        print(x, end = " ")
    print()

if __name__ == "__main__":
    main()