class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3


    def get_num1(self):
        return self.num1

    def get_num2(self):
        return self.num2

    def get_num3(self):
        return self.num3

    def set_num1(self, valor):
        self.num1 = valor

    def set_num2(self, valor):
        self.num2 = valor

    def set_num3(self, valor):
        self.num3 = valor

    def suma(self):
        return self.num1 + self.num2 + self.num3


    def nummayor(self):
        if self.num1 >= self.num2 and self.num1 >= self.num3:
            return self.num1
        elif self.num2 >= self.num1 and self.num2 >= self.num3:
            return self.num2
        else:
            return self.num3



    def  num_menor(self):
        if self.num1 <= self.num2 and self.num1 <= self.num3:
            return self.num1
        elif self.num2 <= self.num1 and self.num2 <= self.num3:
            return self.num2
        else:
            return self.__num3


    def num_iguales(self):
        pass


    def concatenar(self):
        pass