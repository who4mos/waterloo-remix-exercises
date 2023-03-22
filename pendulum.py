from math import cos, sqrt

L = float(input())
A = float(input())

for t in range(10):
    x = L * cos(A * cos(t * sqrt(9.8/L))) - L * cos(A)
    print(x)
