class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3

    def mayor(self):
        if self.__num1 >= self.__num2 and self.__num1 >= self.__num3:
            return self.__num1
        elif self.__num2 >= self.__num3:
            return self.__num2
        else:
            return self.__num3

    def menor(self):
        if self.__num1 <= self.__num2 and self.__num1 <= self.__num3:
            return self.__num1
        elif self.__num2 <= self.__num3:
            return self.__num2
        else:
            return self.__num3

    def iguales(self):
        return self.__num1 == self.__num2 == self.__num3

    def concatenar(self):
        cadena = str(self.__num1) + str(self.__num2) + str(self.__num3)
        return cadena

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

objeto = Mi_Clase(n1, n2, n3)

print("Suma:", objeto.sumar())
print("Mayor:", objeto.mayor())
print("Menor:", objeto.menor())
print("Iguales:", objeto.iguales())
print("Concatenar:", objeto.concatenar())