def take_input():
    return input(), input()

def concat(a, b):
    return a+b

def main():
    a, b = take_input()
    print(concat(a, b))
    output = ""
    for i in range(5):
        output += concat(a, b)
    print(output)

main()
