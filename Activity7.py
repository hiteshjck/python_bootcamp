def take_input():
    a = input("Enter two numbers with a space between them : ")
    #convert string to integers list
    return [int(i) for i in a.split()]

def add(a):
    return sum(a)

def output(a, b):
    print(a[0], "+", a[1], "=", b)

def main():
    a = take_input()
    b = add(a)
    output(a, b)

main()
