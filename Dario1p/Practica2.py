class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        suma = self.__num1 + self.__num2 + self.__num3
        print(f"El resultado de la suma de los 3 numeros es {suma}")

    