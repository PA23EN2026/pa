class Mi_Clase:
    
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
    def sumar(self):
        total = 0
        for n in (self.__num1, self.__num2, self.__num3):
            total += n
        return total
    def mayor(self):
        self.mayor = self.__num1  
        if self.__num2 > self.mayor:
            self.mayor = self.__num2
        if self.__num3 > self.mayor:
            self.mayor = self.__num3
        return self.mayor

    def menor(self):
        self.menor = self.__num1
        if self.__num2 < self.menor:
            self.menor = self.__num2
        if self.__num3 < self.menor:
            self.menor = self.__num3
        return self.menor

    def iguales(self):
        if self.__num1 == self.__num2 and self.__num2 == self.__num3:
            return True
        return False
    
    def concatenar(self):
        return f"{self.__num1}-{self.__num2}-{self.__num3}"
    
# Creacion del objeto
obj = Mi_Clase(5, 10, 5)

# Probar métodos
print("Suma:", obj.sumar())
print("Mayor:", obj.mayor())
print("Menor:", obj.menor())
print("¿Son iguales?:", obj.iguales())
print("Concatenación:", obj.concatenar())