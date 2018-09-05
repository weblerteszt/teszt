#!/usr/bin/env python3

class Example:
    """Ez egy példa osztály"""
    bela = 'alma'
    def gizi(self):
        print('I love you.')
    jozsi = gizi
    def __init__(self):
        self.vali = 24

ex = Example()
ey = Example()

print('Kakukk')

ex.bruno = ['répa']

print(ex.bruno[0])

del(Example.gizi)

print(type(ex))

ex.bela = 'barack'

print(ex.bela)
print(ey.bela)

ex.jozsi()
#ex.gizi()
# AttributeError

message1 = 'Szép '
message2 = 'napot'
message3 = '!'
message = message1 + message2 + message3
print(message)

print('Teszt')
