class Mi_clase:
    def __init_(self,num1,num2,num3):
        self.__num1=num1
        self.__num2=num2
        self.__num3=num3

    def sumar(self):
        result= self.__num1 + self.__num2 + self.__num3 
        return result

    def mayor(self):
        if (self.__num1 > self._num2) and (self.__num1 > self.__num3):
            print(f"El numero mayor es {self.__num1}")
        elif (self.__num2 > self.__num1) and (self.__num2 > self.__num3):
            print(f"El numero mayor es {self.__num2}")
        else:
            print(f"El numero mayor es {self.__num3}")

    def menor(self):
        if (self.__num1 < self._num2) and (self.__num1 < self.__num3):
            print(f"El numero menor es {self.__num1}")
        elif (self.__num2 < self.__num1) and (self.__num2 < self.__num3):
            print(f"El numero menor es {self.__num2}")
        else:
            print(f"El numero menor es {self.__num3}")

    def iguales(self):
        result=(self.__num1==self.__num2) and (self.__num2==self.__num3)
        return result 

    def concatenar(self):
        texto=str(self.__num1)+str(self.__num2)+str(self.__num3)
        return texto 


num1=int(input("Ingresa un numero"))
num2=int(input("Ingresa un numero"))
num3=int(input("Ingresa un numero"))

objeto=Mi_clase(num1,num2,num3)

print(objeto.sumar())
objeto.mayor()
objeto.menor()
print(objeto.iguales())
print(objeto.concatenar())