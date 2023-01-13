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

        if opcion != 7 and opcion != 8 and opcion != 9:
            self.numeros[0] = float(input("Ingresa el primer numero: "))
            self.numeros[1] = float(input("Ingresa el segundo numero: "))
        else:
            self.numeros[0] = float(input("Ingresa el numero: "))


    def mostrar_resultado(self,res):
        print("Resultado: ", res, "\n")


    def suma(self):
        return self.numeros[0] + self.numeros[1]


    def resta(self):
        return self.numeros[0] - self.numeros[1]    


    def multiplicacion(self):
        return self.numeros[0] * self.numeros[1]

    
    def division(self):
        if self.numeros[1] == 0:
            raise ValueError("No es posible la division entre 0")
        else:    
            return self.numeros[0] / self.numeros[1]


    def raiz(self):
        return self.numeros[0] ** (1/self.numeros[1])


    def potencia(self):
        return self.numeros[0] ** self.numeros[1]


    def seno(self):
        return numpy.sin(self.numeros[0])


    def coseno(self):
        return numpy.cos(self.numeros[0])


    def tangente(self):
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

        if opcion == 10:
            calc.apagar()
        elif opcion > 0 and opcion < 9:
            calc.capturar_numeros(opcion)

            if opcion == 1:
                calc.mostrar_resultado(calc.suma())
            elif opcion == 2:
                calc.mostrar_resultado(calc.resta())
            elif opcion == 3:
                calc.mostrar_resultado(calc.multiplicacion())
            elif opcion == 4:
                calc.mostrar_resultado(calc.division())
            elif opcion == 5:
                calc.mostrar_resultado(calc.raiz())
            elif opcion == 6:
                calc.mostrar_resultado(calc.potencia())
            elif opcion == 7:
                calc.mostrar_resultado(calc.seno())
            elif opcion == 8:
                calc.mostrar_resultado(calc.coseno())
            else:
                calc.mostrar_resultado(calc.tangente())
                

if __name__ == '__main__':
    main()
