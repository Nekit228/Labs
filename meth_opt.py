import math
from pylab import * 

#вычисление функции
def f(x):
    return (exp(-2-x) + (x**2)/2)

#Метод дихотомии
dx = 0.01 
l = 0.011   
a = [0]     
b = [1.5]
k = 0

while True:
    yk = (a[k] + b[k] - dx) / 2     
    zk = (a[k] + b[k] + dx) / 2     
    if f(yk) <= f(zk):
        a.append(a[k])  
        b.append(zk)    
    elif f(yk) > f(zk):
        a.append(yk)   
        b.append(b[k])
    l2 = abs(b[k+1] - a[k+1])
    if l2 <= l:
        minx_d = (a[k+1] + b[k+1]) / 2
        break
    elif l2 > l:
        k += 1
        
#Метод золотого сечения
l = 0.1
a = [0]
b = [1.5]
k = 0
y = [a[k] + (3 - sqrt(5)) / 2 * (b[k] - a[k])] 
z = [a[k] + b[k] - y[k]]    


while True:
    if f(y[k]) <= f(z[k]):
        a.append(a[k])
        b.append(z[k])
        y.append(a[k+1] + b[k+1] - y[k])
        z.append(y[k])
    elif f(y[k]) > f(z[k]):
        a.append(y[k])
        b.append(b[k])
        y.append(y[k])
        z.append(a[k+1] + b[k+1] - z[k])
    delta = abs(a[k+1] - b[k+1])
    if delta <= l:
        minx_zs = (a[k+1] + b[k+1]) / 2
        break
    elif delta > l:
        k += 1
    
        
print("Метод дихотомии:", f(minx_d)) 
print("Метод золотого сечения:", f(minx_zs))

xlist = arange(0, 1.5, 0.1)
print(xlist)
#ylist = f(xlist)

#print("Встроенная функция:", min(ylist))
#plot(xlist, ylist)
#show()
