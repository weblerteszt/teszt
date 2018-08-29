#!/usr/bin/env python3

class Complex:
    def __init__(self, realp, imagp):
        self.r = realp
        self.i = imagp
    def print(self):
        print('real: ' + str(self.r) + "\nimag: " + str(self.i))
    def __add__(self, other):
        a = self.r + other.r
        b = self.i + other.i
        return Complex(a, b)

x = Complex(2.0, 4.2)
x.print()
x.r, x.i = 4, 8
x.print()

y = 78.5+-3.6j
print(type(y))

z = 14+2j
w = y + z

print(w)
print(abs(w))