s = input()

for i, c in enumerate(s):
    if c == '+':
        plus_sign = i

n1 = int(s[:plus_sign])
n2 = int(s[plus_sign+1:])

print(n1 + n2)
