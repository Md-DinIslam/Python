# For multiple parameter Add Function...
def add_arg(*num): # variable length argument...
    sum = 0
    for x in num:
        sum += x
    return sum

# Normal Add Function...
def add(a:float, b:float, c:float) -> float:
    return float(a + b + c)

def solve():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    c = float(input("Enter Third Number: "))
    ans = add(a, b, c)
    print("Total Sum: ", ans)
    print("Sum using arguments: ", add_arg(a, b, c, a, b, c))

if __name__ == "__main__":
    solve()