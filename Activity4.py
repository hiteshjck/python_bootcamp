def take_input():
    return int(input("Enter the first number : ")), int(input("Enter the second number : "))

def add(a, b):
    return a+b

def output(a, b, c):
    print(a, "+", b, "=", c)

def main():
    a, b = take_input()
    output(a, b, add(a, b))

main()
