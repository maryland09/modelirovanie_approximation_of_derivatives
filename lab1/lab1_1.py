import matplotlib.pyplot as plt
import math
def f(x):
    return x**(-1)

def ff(x):
    return -1/x**2

def D(x, h):
    return (f(x+h)-f(x-h))/(2*h)

# x0 = 1
# dx0 = ff(x0)
# dx = []
# dy = []
# de = []
# a = math.pow(10, -12)
# b = math.pow(10, -1)
# # a=0
# # b = 100
# h = a
# dh = (b-a)/10.0
# print(a, b, b-a)

# while h < b:
#     h = h + dh
#     dx.append(h)
#     d = D(x0, h)
#     dy.append(d)
#     dif = abs(dx0 - d)
#     de.append(dif)

x0 = 1
dx0 = ff(x0)
dx = []
dy = []
de = []
for i in range(1,13):
    h = 10**(-i)    
    dx.append(h)
    d = D(x0, h)
    dy.append(d)
    dif = abs(dx0 - d)
    de.append(dif)


for i in range(len(dx)):
    print(dx[i], "   ", dy[i], "   ", de[i])

print('       h     |      y(приближ)     |        ошибка      ')
print('-----+---------------+------------')
for h, y, e in zip(dx, dy, de):
    print('{0:.20f}  |   {1:.13f}    |   {2:.13f}'.format(h, y, e))


plt.plot(dx, de, 'g-', linewidth=2)
plt.title('Задача')
plt.xlabel('h')
plt.ylabel('e')
plt.grid(True)
plt.legend(loc=0)
plt.show()



 
    


