print("Jesus Garcia")
#jesumetaru


class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        valores = [self.__num1, self.__num2, self.__num3]
        resultado = sum(valores)
        return resultado
    
    def mayor(self):
        lista_valores = [self.__num1, self.__num2, self.__num3]
        lista_valores.sort()
        return lista_valores[-1] 

    def menor(self):
        lista_valores = [self.__num1, self.__num2, self.__num3]
        lista_valores.sort()
        return lista_valores[0]
    
    def iguales(self):
        if self.__num1 == self.__num2 and self.__num2 == self.__num3:
            return True
        else:
            return False