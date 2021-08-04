def take_input():
    l = float(input("Enter the length of the tromboloid : "))
    b = float(input("Enter the breadth of the tromboloid : "))
    h = float(input("Enter the height of the tromboloid : "))
    return l,b,h

def tromboloid_volume(l, b, h):
    return (b**2 * h**2) / pow( l**2 + b**2 + h**2, 1/2)

def sphere_radius(volume):
    return pow( (3*volume) / (4*3.14), 1/3)

def output(a, b):
    print("Volume of tromboloid: %.3f" %a)
    print("Radius of sphere with same volume: %.3f" %b)

def main():
    l, b, h = take_input()
    vol = tromboloid_volume(l, b, h)
    rad = sphere_radius(vol)
    output(vol, rad)

main()
