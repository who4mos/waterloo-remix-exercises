n = 32

while n <= 127:
    print("chr:", end= " ")
    for i in range(n, n+16):
        if i < 100:
            print(f" {chr(i)}", end="  ")
        else:
            print(f" {chr(i)} ", end=" ")

    print("\nasc:", end=" ")
    for i in range(n, n+16):
        if i < 100:
            print(f"{i}", end="  ")
        else:
            print(f"{i}", end=" ")

    print()
    n += 16
