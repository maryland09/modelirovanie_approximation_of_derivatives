import math

def f(x):
    return math.pow(x, -1)

def f1(x, h):
    return (f(x+h)-f(x-h))/(2*h)

dx = []
dy = []
for i in range(12):
    j = i + 1
    dx.append(-j)
    dy.append(f1(1, 10**(-j)))

x = []


print(dx)
print(dy)

