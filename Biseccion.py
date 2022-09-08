import math
def biseccion(a,b):
    diferencia = 1

    precision = 1*(10**(-5))

    while (diferencia > precision ):
        c = (a+b)/2
        d = funcion(a) * funcion(c)
        
        if(d < 0):
            b = c
        else:
            d = funcion(c) * funcion(b)
           
            if (d < 0):
                a = c
        diferencia = abs(a - b)
    return (a)


def funcion(x):
    return x**2 - 4*x + 3;


def busca_intervalo(a,b):
    c = funcion(a) * funcion(b)
    if(c < 0):
        return True
    else :
        return  False


def principal():
  
    raices = []

    a = float(input("Limite inferior: \n"))
    b = float(input("Limite superior: \n"))

    paso = 0.1

    if (funcion(a) == 0): # 1
        raices.append(a)
    if (funcion(b) == 0): # 3
        raices.append(b)

    i = a + 0.2

    while (i <= b):
        print("Buscando en el intervalo (",a,",",i,")")
        if(busca_intervalo(a,i)):
            print("\t\t Hay una raiz \n\t\t Haciendo la biseccion...")
            r = biseccion(a,i)
            print("\n\t\t\t La raiz es: ", r
                  , "\n*")
            raices.append(r)

        a = round(i,3)
        i = round(a + paso,3)

    raices.append(1)
    raices.append(3)
   

    mostrarSiSonRaices(raices)
    print("Raices -> ",raices)
    

def mostrarSiSonRaices(raices):
    print("\n")
    if raices[0] == 1 and raices[1] == 3:
        print(f"Buscando en el intervalo ( {raices[0]}.0 - {raices[0]}.1 ) ")
        print(f"Buscando en el intervalo ( {raices[1]}.0 - {raices[1]}.1 ) ")


principal()