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
            return True
        else:
            return False



    def concatenar(self):
        return (f"{self.__num1}{self.__num2}{self.__num3}")
    


num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el primer numero: "))
num3 = int(input("Ingresa el primer numero: "))

objeto_num = Mi_Clase(num1, num2, num3)


print(f"La suma es: {objeto_num.suma()}")
print(f"Numero mayor: {objeto_num.nummayor()}")
print(f"Numero menor: {objeto_num.num_menor()}")
print(f"Numeros iguales: {objeto_num.num_iguales()}")
print(f"Concatenar: {objeto_num.concatenar()}")