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

        validarA = True
        validarB = True

        if opcion != 7 and opcion != 8 and opcion != 9:
            
            while validarA:
                try:
                    self.numeros[0] = float(input("Ingrese A: "))
                except ValueError:
                    print("Ingrese número valido\n")
                    continue
                validarA = False

            while validarB:
                try:
                    self.numeros[1] = float(input("Ingrese B: "))
                except ValueError:
                    print("Ingrese número valido\n")
                    continue 

                validarB = False 
        else:
            while validarA:
                try:
                    self.numeros[0] = float(input("Ingrese A: "))
                except ValueError:
                    print("Ingrese número valido\n")
                    continue
                validarA = False


    def mostrar_resultado(self,res):
        print("\nResultado: ", round(res,2), "\n")


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
        if self.numeros[1] == 0:
            raise ValueError("No es posible la division entre 0")
        else:
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
                    1 Sumar A + B
                    2 Restar A - B
                    3 Multiplicar A * B
                    4 Dividir A / B
                    5 Raiz B de A
                    6 Exponente A ^ B
                    7 Seno(A)
                    8 Coseno(A)
                    9 Tangente(A)
                    10 Salir
                """)


def main():

    calc = calculadora()

    while calc.estado():

        calc.menu()
        try:
            opcion = int(input())
        except ValueError:
            continue

        if opcion == 10:
            calc.apagar()
        elif opcion > 0 and opcion < 10:
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
