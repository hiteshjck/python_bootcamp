def take_input():
    return input("Enter 5 numbers with a space between each number : ")

def convert_to_list(a):
    return [int(i) for i in a.split()]

def slice(a):
    return a[:3]

def replace(a):
    # replacing 1st and last element to 0
    a[0], a[-1] = 0, 0
    return a

def output(a, b, c):
    print("sliced list =", a)
    print("replaced list-1 =", b)
    print("replaced list-2 =", c)

def main():
    a = take_input()
    a = convert_to_list(a)
    sliced_list = slice(a)
    replaced_list_1 = replace(a)
    replaced_list_2 = replace(slice(a))
    output(sliced_list, replaced_list_1, replaced_list_2)

main()
