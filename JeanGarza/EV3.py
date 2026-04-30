class Mi_Clase:
    def __init__(self,num1,num2,num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
    
    def sumar(self):
        resultado = self.__num1 + self.__num2 + self.__num3
        print(f"El resultado de la suma de esos tres numero es: {resultado}")
     
    def mayor(self):
        if self.__num1 > self.__num2 and self.__num1 > self.__num3:
            print(f"El numero mayor es: {self.__num1}")
        
        elif self.__num2 > self.__num3:
            print(f"El número mayor es: {self.__num2}")
        
        else:
            print(f"El número mayor es: {self.__num3}")


    @property
    def num1 (self):
        return self.__num1
    


objetosuma = Mi_Clase(2,5,10)
objetosuma.sumar()
print(objetosuma.num1)

objetomayor = Mi_Clase(1,10,100)
objetomayor.mayor()