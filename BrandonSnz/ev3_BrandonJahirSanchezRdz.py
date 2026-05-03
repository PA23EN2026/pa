class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3


    def get_num1(self):
        return self.__num1

    def get_num2(self):
        return self.__num2

    def get_num3(self):
        return self.__num3

    def set_num1(self, valor):
        self.__num1 = valor

    def set_num2(self, valor):
        self.__num2 = valor

    def set_num3(self, valor):
        self.__num3 = valor

    def suma(self):
        return self.__num1 + self.__num2 + self.__num3


    def nummayor(self):
        if self.__num1 >= self.__num2 and self.__num1 >= self.__num3:
            return self.__num1
        elif self.__num2 >= self.__num1 and self.__num2 >= self.__num3:
            return self.__num2
        else:
            return self.__num3



    def  num_menor(self):
        if self.__num1 <= self.__num2 and self.__num1 <= self.__num3:
            return self.__num1
        elif self.__num2 <= self.__num1 and self.__num2 <= self.__num3:
            return self.__num2
        else:
            return self.__num3


    def num_iguales(self):
        if self.__num1 == self.__num2 == self.__num3:
            return(f"Tres numeros iguales Numero1: {self.__num1}, Numero2: {self.__num2}, Numero3: {self.__num3} ")
        elif self.__num1 == self.__num2:
            return(f"Dos numeros iguales 1 y 2 \nNumero1: {self.__num1}, \nNumero2: {self.__num2}, \nNumero3: {self.__num3}")
        elif self.__num1 == self.__num3:
            return (f"Dos numeros iguales 1 y 3 \nNumero1: {self.__num1}, \nNumero2: {self.__num2}, \nNumero3: {self.__num3} ")
        elif self.__num2 == self.__num3:
            return (f"Dos numeros iguales 2 y 3 \nNumero1: {self.__num1}, \nNumero2: {self.__num2}, \nNumero3: {self.__num3} ")
        else:
            return "Ningun numero es igual"



    def concatenar(self):
        pass
    