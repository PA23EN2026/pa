class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
        

    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3

    def mayor(self):
        return max(self.__num1, self.__num2, self.__num3)

    def menor(self):
        return min(self.__num1, self.__num2, self.__num3)

    def iguales(self):
        return self.__num1 == self.__num2 == self.__num3

    def concatenar(self):
        return str(self.__num1) + str(self.__num2) + str(self.__num3)

    
obj = Mi_Clase(10, 20, 30)

print("Suma:", obj.sumar())
print("Mayor:", obj.mayor())
print("Menor:", obj.menor())
print("¿Son iguales?:", obj.iguales())
print("Concatenación:", obj.concatenar())