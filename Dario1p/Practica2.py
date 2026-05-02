class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        suma = self.__num1 + self.__num2 + self.__num3
        return suma

    def mayor(self):
        if self.__num1 > self.__num2 and self.__num1 > self.__num3:
            return self.__num1
        elif self.__num2 > self.__num3:
            return self.__num2
        else:
            return self.__num3
        
    def menor (self):
        if self.__num1 < self.__num2 and self.__num1 < self.__num3:
            return self.__num1
        elif self.__num2 < self.__num3:
            return self.__num2
        else:
            return self.__num3
    
    def iguales (self):
        Igualdad = False

        if self.__num1 == self.__num2 and self.__num2 == self.__num3:
            Igualdad = True

        return Igualdad
    
    def concatenar(self):
        return (f"{self.__num1}{self.__num2}{self.__num3}") 

####################################################################################
num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))
num3 = int(input("Dime el tercer numero: "))
objeto_clase = Mi_Clase(num1, num2, num3)

print(f"La suma de los 3 numeros son: {objeto_clase.sumar()}")  
print(f"El numero mayor es: {objeto_clase.mayor()}")
print(f"El numero menor es: {objeto_clase.menor()}")
print(f"Los numeros son iguales: {objeto_clase.iguales()}")
print(f"Los numeros concatenados son: {objeto_clase.concatenar()}")

    
    