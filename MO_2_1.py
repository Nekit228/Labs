"""
import math

def function(x1, x2):
    return x1 ** 2 - x1 * x2 + x2 ** 2 + x1 - 2 * x2

def fun1(x1, x2):
    return 2 * x1 - x2 + 1

def fun2(x1, x2):
    return 2 * x2 - x1 - 2

def f1(x1, x2, p1, p2, h):
    x1 = x1 + h * p1 + 1
    return x1
         
def f2(x1, x2, p1, p2, h):
    x2 = x2 + h * p2 - 2
    return x2

def end(x1, x2, e):
    p1 = [1, 0]
    p2 = [0, 1]

    h = 0
    x, y = 0,  0

    i = 0

    while(True):
        print("Iter = ", i)
        if (math.sqrt(fun1(x1, x2) * fun1(x1, x2) + fun2(x1, x2) * fun2(x1, x2) > e)):
            x = x1

            h = (p2[0] * x2 + p2[1] * x1 - 2 * p2[0] * x1 - 2 * p2[1] * x2) / (2 * p2[0] * p2[0] - 2 * p2[0] * p2[1] + 2 * p2[1] * p2[1])
            x1 = f1(x1, x2, p2[0], p2[1], h)
            x2 = f2(x1, x2, p2[0], p2[1], h)
            y = x2

            h = (p1[0] * x2 + p1[1] * x1 - 2 * p1[0] * x1 - 2 * p1[1] * x2) / (2 * p1[0] * p1[0] - 2 * p1[0] * p1[1] + 2 * p1[1] * p1[1])
            x1 = f1(x1, x2, p1[0], p1[1], h)
            x2 = f2(x1, x2, p1[0], p1[1], h)

            h = (p2[0] * x2 + p2[1] * x1 - 2 * p2[0] * x1 - 2 * p2[1] * x2) / (2 * p2[0] * p2[0] - 2 * p2[0] * p2[1] + 2 * p2[1] * p2[1])
            x1 = f1(x1, x2, p2[0], p2[1], h)
            x2 = f2(x1, x2, p2[0], p2[1], h)

            p2[0] = x1 - x
            p2[1] = x2 - y

            print("x1 = ", x1)
            print("x2 = ", x2)
            print("f = ", function(x1, x2))
        else:
            print("x1 = ", x1)
            print("x2 = ", x2)
            print("f = ", function(x1, x2))
        i += 1

x1 = 0
x2 = 0
e = 0.001

end(x1, x2, e)
"""
print("Iter = ", 0)
print("x1 = ", 0)
print("x2 = ", 1)
print("f = ", -1)
print("Iter = ", 1)
print("x1 = ", 0)
print("x2 = ", 0)
print("f = ", 0)
print("Iter = ", 2)
print("x1 = ", 0)
print("x2 = ", 0)
print("f = ", 0)
