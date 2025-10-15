# variable length argument...
def add_arg(*num): 
    sum = 0
    for x in num:
        sum += x
    return sum

# default Argument...
def print_info(name, university = "BRAC"):
    print("Name: ", name)
    print("University: ", university)

def default_argument():
    print_info("Din")
    print()
    print_info("Din", "GUB")

def solve():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    c = float(input("Enter Third Number: "))
    print("Sum using arguments: ", add_arg(a, b, c))
    print()
    
    default_argument()

if __name__ == "__main__":
    solve()