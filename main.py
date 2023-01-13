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
        return int(input())



def main():

    calc = calculadora()

    while calc.estado():

        opcion = calc.menu()

        if opcion != 10:
            numeros = calc.capturar_numeros(opcion)
        else:
            calc.apagar()    

if __name__ == '__main__':
    main()
