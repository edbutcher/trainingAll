#__________________________________
import math

def square(r):
    s =  math.pi * (r**2)
    return print("S=", s)
r = int(input('tape radius:'))
square(r)

#__________________________________
def twowords(x, y):
    return (x + ', ' + y)

x, y = input("first word:"), input("second word:")
print(twowords(x, y))


#__________________________________
def x_between_ab(a, b, x):
    return (a < x < b or a > x > b)

def y(y):
    return (int(input(y)))

a, b, x = y('a:'), y('b:'), y('x:')
print(x_between_ab(a, b, x))


#__________________________________
def square_abc(a, b, c):
    x1 = ((-b) + (b * 2 - 4 * a * c) * 0.5) / 2*a
    x2 = ((-b) - (b * 2 - 4 * a * c) * 0.5) / 2*a
    return (x1, x2)

def y(y):
    return (int(input(y)))

a, b, c = y('a:'), y('b:'), y('c:')
print(square_abc(a, b, c))
