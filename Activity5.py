def take_input():
    return input("Enter 5 numbers with a space between each number : ")

def convert_to_list(a):
    return a.split()

def add_list(a):
    # convert list elements from string to integers
    a = [int(i) for i in a]
    return sum(a)

def output(a):
    print("Sum of all the numbers is =", a)

def main():
    a = take_input()
    a = convert_to_list(a)
    a = add_list(a)
    output(a)

main()
