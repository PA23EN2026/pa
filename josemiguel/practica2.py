class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3
    
    def mayor(self):
        mayor = self.__num1
        if self.__num2 > mayor:
            mayor = self.__num2
        if self.__num3 > mayor:
            mayor = self.__num3
        return mayor

    def menor(self):
        menor = self.__num1
        if self.__num2 < menor:
            menor = self.__num2
        if self.__num3 < menor:
            menor = self.__num3
        return menor
    
    def iguales(self):
        return self.__num1 == self.__num2 == self.__num3
    
    def concatenar(self):
        return str(self.__num1) + str(self.__num2) + str(self.__num3)
    
#PRUEBA DE COMO SE VERIA CON UN MENU INTEGRADO

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

obj = Mi_Clase(num1, num2, num3)

print("n1 Sumar")
print("n2 Mayor")
print("n3 Menor")
print("n4 Iguales")
print("n5 Concatenar")

