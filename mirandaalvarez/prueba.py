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
    
prueba=Mi_Clase(9,9,9)

print("Suma:",prueba.sumar())
print("Mayor:",prueba.mayor())
print("Menor:",prueba.menor())
print("Son iguales?:",prueba.iguales())
print("Concatenación:",prueba.concatenar())


