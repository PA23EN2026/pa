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
        elif self.__num2 >= self.__num1 and self.__num2 >= self.__num3:
            return self.__num2
        else:
            return self.__num3
    
    def menor(self):
        if self.__num1 <= self.__num2 and self.__num1 <= self.__num3:
            return self.__num1
        elif self.__num2 <= self.__num1 and self.__num2 <= self.__num3:
            return self.__num2
        else:
            return self.__num3 
        
    def iguales(self):
        return self.__num1 == self.__num2 == self.__num3
    
    def concatenar(self):
        return str(self.__num1) + str(self.__num2) + str(self.__num3)
    
objeto = Mi_Clase(10,22,30)
print(f"La suma de los numeros es: {objeto.sumar()}")
print(f"El numero mayor es: {objeto.mayor()}")
print(f"El numero menor es: {objeto.menor()}")
print(f"¿Son iguales?: {objeto.iguales()}")
print(f"Concatenar: {objeto.concatenar()}")               