import numpy

class calculadora():

    def __init__(self):
        self.numeros = [0,0]
        self.encendido = True 

    def estado(self):
        return self.encendido

    def apagar(self):
        self.encendido = False


    def capturar_numeros(self,opcion):

        if opcion != 5 and opcion != 6:
            self.numeros[0] = float(input("Ingresa el primer numero: "))
            self.numeros[1] = float(input("Ingresa el segundo numero: "))
        else:
            self.numeros[0] = float(input("Ingresa el numero: "))
            self.numeros[1] = float(input("Ingresa la potencia: "))

        return self.numeros


    def suma(self,numeros):
        return self.numeros[0] + self.numeros[1]


    def resta(self,numeros):
        return self.numeros[0] - self.numeros[1]    


    def multiplicacion(self,numeros):
        return self.numeros[0] * self.numeros[1]

    
    def division(self,numeros):
        if numeros[1] == 0:
            raise ValueError("No es posible la division entre 0")
            
        return self.numeros[0] / self.numeros[1]


    def raiz(self,numeros):
        return self.numeros[0] ** (1/self.numeros[1])


    def potencia(self,numeros):
        return self.numeros[0] ** self.numeros[1]


    def seno(self,numeros):
        return numpy.sin(self.numeros[0])


    def coseno(self,numeros):
        return numpy.cos(self.numeros[0])


    def tangente(self,numeros):
        return numpy.tan(self.numeros[0])


    def menu(self):
        print("""
                Seleccione una opción:
                    1 Sumar
                    2 Restar
                    3 Multiplicar
                    4 Dividir
                    5 Raiz n
                    6 Exponente n
                    7 Seno
                    8 Coseno
                    9 Tangente
                    10 Salir
                """)


def main():

    calc = calculadora()

    while calc.estado():

        calc.menu()
        opcion = int(input())

        if opcion != 10:
            numeros = calc.capturar_numeros(opcion)

            print("El resultado es: ", calc.seno(numeros), "\n")
        else:
            calc.apagar()    

if __name__ == '__main__':
    main()
