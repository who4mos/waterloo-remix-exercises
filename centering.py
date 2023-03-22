from math import ceil, floor

width = int(input())

s = input()

while s != "END":
    dots = width - len(s)

    if dots == 0:
        print(s)
    elif dots % 2 == 1:
        print(f"{'.' * ceil(dots/2)}{s}{'.' * floor(dots/2)}")
    else:
        print(f"{'.' * (dots//2)}{s}{'.' * (dots//2)}")

    s = input()
