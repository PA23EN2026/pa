print("Jesus Garcia")
#jesumetaru


class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        print("Entrando al metodo sumar")
        valores = [self.__num1, self.__num2, self.__num3]
        resultado = sum(valores)
        return resultado