#Phyton Numbers
#Para tipos de numero los podemos definir como int, float y complex
x = 90      #int
y = 20.5    #Float
z = 6j      #Complex
print(type(x))
print(type(y))
print(type(z))

#Int
o = 50
p = 222222255555555
q = -1452600000
print(type(o))
print(type(p))
print(type(q))

#Float
x = 50.99
y = 50.0
z = -66.55
print(type(x))
print(type(y))
print(type(z))

#Complex
a = 8+6j
b = 8j
c = -8j
print(type(a))
print(type(b))
print(type(c))

#Type Conversion
d = 80
e = 8.41
f = 62j
print(d)
print(e)
print(f)

g = float(d)
h = int(e)
i = complex(d)

print("De Entero a Flotante: " , g)
print(type(g))
print("De Flotante a Entero: " , h)
print(type(h))
print("De Entero a Complejo: " , i)
print(type(i))

#Random Number
import random
print("El numero random entre 1 a 100 es: " ,random.randrange(1,100))