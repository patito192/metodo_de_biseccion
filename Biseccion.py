import math
from turtle import color
from matplotlib import pyplot

def metodo_biseccion(funcion, x_a, x_b, piso=None, pasos=10000):
    if funcion(x_a)*funcion(x_b) >= 0:
        print("error")
        return None;

    for n in range(pasos + 1):
        punto_medio = (x_a + x_b) / 2

        if funcion(punto_medio) == 0:
            return punto_medio

        if funcion(x_a)*funcion(punto_medio) < 0:
            x_b = punto_medio
        else:
            x_a = punto_medio

    return (x_a + x_b) / 2

def funcion_a_graficar(x):
    return x*x + 2*x -8

range_for_graphic = range(0,100);

pyplot.plot(range_for_graphic, [funcion_a_graficar(i) for i in range_for_graphic])

pyplot.axhline(0, color="blue")
pyplot.axvline(0, color="blue")

pyplot.xlim(-10, 10)
pyplot.ylim(-10,10)

pyplot.show()

    
x = int(input("Ingresa el x: "))
y = int(input("Ingresa el y: "))

funcion_a_resolver = lambda x: x**2 + 2*x - 8

resultado = metodo_biseccion(funcion_a_resolver, x, y, 1e-3);

print(resultado)