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

    def menor(self):
        menor = self.__num1
        if self.__num2 < menor:
            menor = self.__num2
        if self.__num3 < menor:
            menor = self.__num3
    
    def iguales(self):
        if self.__num1 == self.__num2 and self.__num2 == self.__num3:
            return True
        return False