"""
Napisać moduł geometry zawierajacy funkcję do obliczania pola
kilku figur (kwadrat, prostokat, koło). Przetestować jego działanie
przykładowym programem.
"""

def square(x):
    return x ** 2

def rectangle(x, y):
    return x * y

def triangle(a, h):
    return (a * h)/ 2

def circle(r):
    return 3,14 * r ** 2

def rhombus(e, f):
    return (e * f) / 2

def trapezium(a, b, h):
    return (a+b)*h / 2

